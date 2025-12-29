#!/bin/bash
#
# VNTS Server Installation Script
# Supports: Debian/Ubuntu, CentOS/RHEL/Fedora, Arch, Alpine, openSUSE
# Architectures: x86_64, aarch64, armv7, arm, mips, mipsel
#
# Usage: bash install-vnts.sh [options]
#   Options:
#     --port PORT        Server port (default: 29872)
#     --web-port PORT    Web admin port (default: 29870)
#     --gateway IP       Virtual network gateway (default: 10.26.0.1)
#     --netmask MASK     Virtual network netmask (default: 255.255.255.0)
#     --token TOKEN      Token whitelist (comma-separated)
#     --web              Enable web admin interface (disabled by default)
#     --uninstall        Uninstall vnts
#     --update           Update to latest version
#     -h, --help         Show this help message
#

set -e

# ==================== Configuration ====================
VNTS_VERSION="1.2.12"
INSTALL_DIR="/opt/vnts"
BIN_DIR="/usr/local/bin"
SERVICE_NAME="vnts"
GITHUB_REPO="vnt-dev/vnts"
DEFAULT_PORT=29872
DEFAULT_WEB_PORT=29870
DEFAULT_GATEWAY="10.26.0.1"
DEFAULT_NETMASK="255.255.255.0"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# ==================== Helper Functions ====================

log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
    exit 1
}

check_root() {
    if [[ $EUID -ne 0 ]]; then
        log_error "This script must be run as root. Use: sudo bash $0"
    fi
}

# ==================== System Detection ====================

detect_os() {
    if [[ -f /etc/os-release ]]; then
        . /etc/os-release
        OS=$ID
        OS_VERSION=$VERSION_ID
        OS_NAME=$PRETTY_NAME
    elif [[ -f /etc/redhat-release ]]; then
        OS="centos"
        OS_NAME=$(cat /etc/redhat-release)
    elif [[ -f /etc/debian_version ]]; then
        OS="debian"
        OS_NAME="Debian $(cat /etc/debian_version)"
    else
        log_error "Unsupported operating system"
    fi

    log_info "Detected OS: $OS_NAME"
}

detect_arch() {
    ARCH=$(uname -m)
    case $ARCH in
        x86_64|amd64)
            VNTS_ARCH="x86_64-unknown-linux-musl"
            ;;
        aarch64|arm64)
            VNTS_ARCH="aarch64-unknown-linux-musl"
            ;;
        armv7l|armv7)
            VNTS_ARCH="armv7-unknown-linux-musleabihf"
            ;;
        armv6l|arm)
            VNTS_ARCH="arm-unknown-linux-musleabihf"
            ;;
        mips)
            VNTS_ARCH="mips-unknown-linux-musl"
            ;;
        mipsel|mips64el)
            VNTS_ARCH="mipsel-unknown-linux-musl"
            ;;
        *)
            log_error "Unsupported architecture: $ARCH"
            ;;
    esac

    log_info "Detected architecture: $ARCH -> $VNTS_ARCH"
}

detect_init_system() {
    if command -v systemctl &> /dev/null && pidof systemd &> /dev/null; then
        INIT_SYSTEM="systemd"
    elif command -v rc-service &> /dev/null; then
        INIT_SYSTEM="openrc"
    elif command -v service &> /dev/null; then
        INIT_SYSTEM="sysvinit"
    else
        INIT_SYSTEM="unknown"
        log_warn "Unknown init system, service management may not work"
    fi

    log_info "Detected init system: $INIT_SYSTEM"
}

detect_firewall() {
    if command -v firewall-cmd &> /dev/null && systemctl is-active firewalld &> /dev/null 2>&1; then
        FIREWALL="firewalld"
    elif command -v ufw &> /dev/null && ufw status 2>/dev/null | grep -q "Status: active"; then
        FIREWALL="ufw"
    elif command -v iptables &> /dev/null; then
        FIREWALL="iptables"
    elif command -v nft &> /dev/null; then
        FIREWALL="nftables"
    else
        FIREWALL="none"
    fi

    log_info "Detected firewall: $FIREWALL"
}

detect_package_manager() {
    if command -v apt-get &> /dev/null; then
        PKG_MANAGER="apt"
    elif command -v dnf &> /dev/null; then
        PKG_MANAGER="dnf"
    elif command -v yum &> /dev/null; then
        PKG_MANAGER="yum"
    elif command -v pacman &> /dev/null; then
        PKG_MANAGER="pacman"
    elif command -v apk &> /dev/null; then
        PKG_MANAGER="apk"
    elif command -v zypper &> /dev/null; then
        PKG_MANAGER="zypper"
    else
        PKG_MANAGER="unknown"
    fi

    log_info "Detected package manager: $PKG_MANAGER"
}

# ==================== Dependency Installation ====================

install_dependencies() {
    log_info "Installing dependencies..."

    case $PKG_MANAGER in
        apt)
            apt-get update -qq
            apt-get install -y -qq curl wget tar
            ;;
        dnf)
            dnf install -y -q curl wget tar
            ;;
        yum)
            yum install -y -q curl wget tar
            ;;
        pacman)
            pacman -Sy --noconfirm --quiet curl wget tar
            ;;
        apk)
            apk add --no-cache curl wget tar
            ;;
        zypper)
            zypper install -y curl wget tar
            ;;
        *)
            log_warn "Unknown package manager, assuming dependencies are installed"
            ;;
    esac

    log_success "Dependencies installed"
}

# ==================== Firewall Configuration ====================

configure_firewall() {
    local port=$1
    local web_port=$2
    local enable_web=$3

    log_info "Configuring firewall for port $port (TCP/UDP)..."

    case $FIREWALL in
        firewalld)
            configure_firewalld "$port" "$web_port" "$enable_web"
            ;;
        ufw)
            configure_ufw "$port" "$web_port" "$enable_web"
            ;;
        iptables)
            configure_iptables "$port" "$web_port" "$enable_web"
            ;;
        nftables)
            configure_nftables "$port" "$web_port" "$enable_web"
            ;;
        none)
            log_warn "No active firewall detected, skipping firewall configuration"
            log_warn "Please manually open port $port (TCP/UDP) if you have a firewall"
            if [[ "$enable_web" != "true" ]]; then
                log_warn "WARNING: vnts web interface is ALWAYS enabled on port $web_port by default!"
                log_warn "Without a firewall, the web interface will be exposed to the network."
                log_warn "Consider blocking port $web_port manually or using --web to acknowledge this."
            fi
            return
            ;;
    esac

    log_success "Firewall configured successfully"
}

configure_firewalld() {
    local port=$1
    local web_port=$2
    local enable_web=$3

    # Open main port
    firewall-cmd --permanent --add-port=${port}/tcp
    firewall-cmd --permanent --add-port=${port}/udp

    # Web port: open if enabled, explicitly block if not
    if [[ "$enable_web" == "true" ]]; then
        firewall-cmd --permanent --add-port=${web_port}/tcp
        log_info "Web interface enabled on port ${web_port}"
    else
        # Remove web port rule if exists (in case of previous --web install)
        firewall-cmd --permanent --remove-port=${web_port}/tcp 2>/dev/null || true
        log_info "Web port ${web_port} blocked from external access (vnts still runs it locally)"
    fi

    firewall-cmd --reload
}

configure_ufw() {
    local port=$1
    local web_port=$2
    local enable_web=$3

    # Open main port
    ufw allow ${port}/tcp
    ufw allow ${port}/udp

    # Web port: open if enabled, explicitly deny if not
    if [[ "$enable_web" == "true" ]]; then
        ufw allow ${web_port}/tcp
        log_info "Web interface enabled on port ${web_port}"
    else
        # Deny web port from external access
        ufw delete allow ${web_port}/tcp 2>/dev/null || true
        ufw deny ${web_port}/tcp 2>/dev/null || true
        log_info "Web port ${web_port} blocked from external access (vnts still runs it locally)"
    fi

    # Ensure ufw is enabled
    echo "y" | ufw enable 2>/dev/null || true
}

configure_iptables() {
    local port=$1
    local web_port=$2
    local enable_web=$3

    # Open main port
    iptables -I INPUT -p tcp --dport ${port} -j ACCEPT
    iptables -I INPUT -p udp --dport ${port} -j ACCEPT

    # Web port: open if enabled, explicitly drop if not
    if [[ "$enable_web" == "true" ]]; then
        iptables -I INPUT -p tcp --dport ${web_port} -j ACCEPT
        log_info "Web interface enabled on port ${web_port}"
    else
        # Remove any existing ACCEPT rule for web port
        iptables -D INPUT -p tcp --dport ${web_port} -j ACCEPT 2>/dev/null || true
        # Add DROP rule for web port (external access blocked)
        iptables -I INPUT -p tcp --dport ${web_port} -j DROP
        log_info "Web port ${web_port} blocked from external access (vnts still runs it locally)"
    fi

    # Save iptables rules (varies by distro)
    if command -v iptables-save &> /dev/null; then
        case $OS in
            debian|ubuntu)
                if [[ -d /etc/iptables ]]; then
                    iptables-save > /etc/iptables/rules.v4
                else
                    mkdir -p /etc/iptables
                    iptables-save > /etc/iptables/rules.v4
                fi
                ;;
            centos|rhel|fedora|rocky|almalinux)
                if command -v service &> /dev/null; then
                    service iptables save 2>/dev/null || iptables-save > /etc/sysconfig/iptables
                else
                    iptables-save > /etc/sysconfig/iptables
                fi
                ;;
            *)
                log_warn "Could not save iptables rules automatically. Rules may not persist after reboot."
                ;;
        esac
    fi
}

configure_nftables() {
    local port=$1
    local web_port=$2
    local enable_web=$3

    # Create vnts table and chain if not exists
    nft add table inet vnts 2>/dev/null || true
    nft add chain inet vnts input { type filter hook input priority 0 \; } 2>/dev/null || true

    # Open main port
    nft add rule inet vnts input tcp dport ${port} accept
    nft add rule inet vnts input udp dport ${port} accept

    # Web port: open if enabled, explicitly drop if not
    if [[ "$enable_web" == "true" ]]; then
        nft add rule inet vnts input tcp dport ${web_port} accept
        log_info "Web interface enabled on port ${web_port}"
    else
        # Drop external access to web port
        nft add rule inet vnts input tcp dport ${web_port} drop
        log_info "Web port ${web_port} blocked from external access (vnts still runs it locally)"
    fi

    # Save rules
    if [[ -f /etc/nftables.conf ]]; then
        nft list ruleset > /etc/nftables.conf
    fi
}

remove_firewall_rules() {
    local port=$1
    local web_port=$2

    log_info "Removing firewall rules..."

    case $FIREWALL in
        firewalld)
            firewall-cmd --permanent --remove-port=${port}/tcp 2>/dev/null || true
            firewall-cmd --permanent --remove-port=${port}/udp 2>/dev/null || true
            firewall-cmd --permanent --remove-port=${web_port}/tcp 2>/dev/null || true
            firewall-cmd --reload
            ;;
        ufw)
            ufw delete allow ${port}/tcp 2>/dev/null || true
            ufw delete allow ${port}/udp 2>/dev/null || true
            ufw delete allow ${web_port}/tcp 2>/dev/null || true
            ;;
        iptables)
            iptables -D INPUT -p tcp --dport ${port} -j ACCEPT 2>/dev/null || true
            iptables -D INPUT -p udp --dport ${port} -j ACCEPT 2>/dev/null || true
            iptables -D INPUT -p tcp --dport ${web_port} -j ACCEPT 2>/dev/null || true
            ;;
        nftables)
            nft delete table inet vnts 2>/dev/null || true
            ;;
    esac

    log_success "Firewall rules removed"
}

# ==================== Download & Installation ====================

get_latest_version() {
    log_info "Checking latest version..."

    local latest_version
    latest_version=$(curl -sL "https://api.github.com/repos/${GITHUB_REPO}/releases/latest" | grep '"tag_name":' | sed -E 's/.*"v?([^"]+)".*/\1/')

    if [[ -n "$latest_version" ]]; then
        VNTS_VERSION="$latest_version"
        log_info "Latest version: v$VNTS_VERSION"
    else
        log_warn "Could not fetch latest version, using default: v$VNTS_VERSION"
    fi
}

download_vnts() {
    log_info "Downloading vnts v${VNTS_VERSION} for ${VNTS_ARCH}..."

    local download_url="https://github.com/${GITHUB_REPO}/releases/download/v${VNTS_VERSION}/vnts-${VNTS_ARCH}-v${VNTS_VERSION}.tar.gz"
    local temp_file="/tmp/vnts.tar.gz"

    log_info "Download URL: $download_url"

    if command -v wget &> /dev/null; then
        wget -q --show-progress -O "$temp_file" "$download_url" || log_error "Download failed"
    elif command -v curl &> /dev/null; then
        curl -L -o "$temp_file" "$download_url" || log_error "Download failed"
    else
        log_error "Neither wget nor curl is available"
    fi

    log_success "Download completed"
}

install_vnts() {
    local temp_file="/tmp/vnts.tar.gz"
    local temp_dir="/tmp/vnts_extract"

    log_info "Installing vnts to $INSTALL_DIR..."

    # Create installation directory
    mkdir -p "$INSTALL_DIR"
    mkdir -p "$INSTALL_DIR/log"
    mkdir -p "$INSTALL_DIR/key"

    # Extract
    rm -rf "$temp_dir"
    mkdir -p "$temp_dir"
    tar -xzf "$temp_file" -C "$temp_dir"

    # Find and copy the binary
    local vnts_binary
    vnts_binary=$(find "$temp_dir" -name "vnts" -type f | head -1)

    if [[ -z "$vnts_binary" ]]; then
        log_error "vnts binary not found in archive"
    fi

    cp "$vnts_binary" "$INSTALL_DIR/vnts"
    chmod +x "$INSTALL_DIR/vnts"

    # Create symlink
    ln -sf "$INSTALL_DIR/vnts" "$BIN_DIR/vnts"

    # Cleanup
    rm -rf "$temp_file" "$temp_dir"

    log_success "vnts installed to $INSTALL_DIR"
}

# ==================== Service Configuration ====================

create_systemd_service() {
    local port=$1
    local web_port=$2
    local enable_web=$3
    local token=$4
    local gateway=$5
    local netmask=$6

    log_info "Creating systemd service..."

    local extra_args=""
    # Add gateway and netmask
    extra_args="$extra_args -g $gateway -m $netmask"
    if [[ "$enable_web" == "true" ]]; then
        extra_args="$extra_args --web-port $web_port"
    fi
    if [[ -n "$token" ]]; then
        extra_args="$extra_args -w $token"
    fi

    cat > /etc/systemd/system/${SERVICE_NAME}.service << EOF
[Unit]
Description=VNT Server - Virtual Network Tool Server
Documentation=https://github.com/${GITHUB_REPO}
After=network.target network-online.target
Wants=network-online.target

[Service]
Type=simple
User=root
Group=root
WorkingDirectory=${INSTALL_DIR}
ExecStart=${INSTALL_DIR}/vnts -p ${port}${extra_args}
ExecReload=/bin/kill -HUP \$MAINPID
Restart=on-failure
RestartSec=5
LimitNOFILE=1048576
LimitNPROC=512

# Security hardening
NoNewPrivileges=true
ProtectSystem=strict
ProtectHome=true
ReadWritePaths=${INSTALL_DIR}
PrivateTmp=true

[Install]
WantedBy=multi-user.target
EOF

    systemctl daemon-reload
    log_success "Systemd service created"
}

create_openrc_service() {
    local port=$1
    local web_port=$2
    local enable_web=$3
    local token=$4
    local gateway=$5
    local netmask=$6

    log_info "Creating OpenRC service..."

    local extra_args=""
    # Add gateway and netmask
    extra_args="$extra_args -g $gateway -m $netmask"
    if [[ "$enable_web" == "true" ]]; then
        extra_args="$extra_args --web-port $web_port"
    fi
    if [[ -n "$token" ]]; then
        extra_args="$extra_args -w $token"
    fi

    cat > /etc/init.d/${SERVICE_NAME} << EOF
#!/sbin/openrc-run

name="vnts"
description="VNT Server - Virtual Network Tool Server"
command="${INSTALL_DIR}/vnts"
command_args="-p ${port}${extra_args}"
command_background=true
pidfile="/run/\${RC_SVCNAME}.pid"
directory="${INSTALL_DIR}"

depend() {
    need net
    after firewall
}

start_pre() {
    checkpath --directory --owner root:root --mode 0755 ${INSTALL_DIR}/log
}
EOF

    chmod +x /etc/init.d/${SERVICE_NAME}
    log_success "OpenRC service created"
}

create_sysvinit_service() {
    local port=$1
    local web_port=$2
    local enable_web=$3
    local token=$4
    local gateway=$5
    local netmask=$6

    log_info "Creating SysVinit service..."

    local extra_args=""
    # Add gateway and netmask
    extra_args="$extra_args -g $gateway -m $netmask"
    if [[ "$enable_web" == "true" ]]; then
        extra_args="$extra_args --web-port $web_port"
    fi
    if [[ -n "$token" ]]; then
        extra_args="$extra_args -w $token"
    fi

    cat > /etc/init.d/${SERVICE_NAME} << 'INITSCRIPT'
#!/bin/bash
### BEGIN INIT INFO
# Provides:          vnts
# Required-Start:    $network $remote_fs
# Required-Stop:     $network $remote_fs
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: VNT Server
# Description:       Virtual Network Tool Server
### END INIT INFO

INITSCRIPT

    cat >> /etc/init.d/${SERVICE_NAME} << EOF

DAEMON="${INSTALL_DIR}/vnts"
DAEMON_ARGS="-p ${port}${extra_args}"
PIDFILE="/var/run/${SERVICE_NAME}.pid"
LOGFILE="${INSTALL_DIR}/log/vnts.log"

start() {
    echo "Starting vnts..."
    cd ${INSTALL_DIR}
    nohup \$DAEMON \$DAEMON_ARGS >> \$LOGFILE 2>&1 &
    echo \$! > \$PIDFILE
    echo "vnts started"
}

stop() {
    echo "Stopping vnts..."
    if [ -f \$PIDFILE ]; then
        kill \$(cat \$PIDFILE) 2>/dev/null
        rm -f \$PIDFILE
    fi
    echo "vnts stopped"
}

status() {
    if [ -f \$PIDFILE ] && kill -0 \$(cat \$PIDFILE) 2>/dev/null; then
        echo "vnts is running (PID: \$(cat \$PIDFILE))"
    else
        echo "vnts is not running"
    fi
}

case "\$1" in
    start)   start ;;
    stop)    stop ;;
    restart) stop; start ;;
    status)  status ;;
    *)       echo "Usage: \$0 {start|stop|restart|status}"; exit 1 ;;
esac
EOF

    chmod +x /etc/init.d/${SERVICE_NAME}
    log_success "SysVinit service created"
}

create_service() {
    local port=$1
    local web_port=$2
    local enable_web=$3
    local token=$4
    local gateway=$5
    local netmask=$6

    case $INIT_SYSTEM in
        systemd)
            create_systemd_service "$port" "$web_port" "$enable_web" "$token" "$gateway" "$netmask"
            ;;
        openrc)
            create_openrc_service "$port" "$web_port" "$enable_web" "$token" "$gateway" "$netmask"
            ;;
        sysvinit)
            create_sysvinit_service "$port" "$web_port" "$enable_web" "$token" "$gateway" "$netmask"
            ;;
        *)
            log_warn "Unknown init system, skipping service creation"
            log_warn "You can start vnts manually: ${INSTALL_DIR}/vnts -p ${port} -g ${gateway} -m ${netmask}"
            ;;
    esac
}

enable_and_start_service() {
    log_info "Enabling and starting vnts service..."

    case $INIT_SYSTEM in
        systemd)
            systemctl enable ${SERVICE_NAME}
            systemctl start ${SERVICE_NAME}
            sleep 2
            if systemctl is-active --quiet ${SERVICE_NAME}; then
                log_success "vnts service is running"
            else
                log_error "Failed to start vnts service. Check: journalctl -u ${SERVICE_NAME}"
            fi
            ;;
        openrc)
            rc-update add ${SERVICE_NAME} default
            rc-service ${SERVICE_NAME} start
            ;;
        sysvinit)
            update-rc.d ${SERVICE_NAME} defaults 2>/dev/null || chkconfig ${SERVICE_NAME} on 2>/dev/null || true
            /etc/init.d/${SERVICE_NAME} start
            ;;
    esac
}

stop_and_disable_service() {
    log_info "Stopping and disabling vnts service..."

    case $INIT_SYSTEM in
        systemd)
            systemctl stop ${SERVICE_NAME} 2>/dev/null || true
            systemctl disable ${SERVICE_NAME} 2>/dev/null || true
            rm -f /etc/systemd/system/${SERVICE_NAME}.service
            systemctl daemon-reload
            ;;
        openrc)
            rc-service ${SERVICE_NAME} stop 2>/dev/null || true
            rc-update del ${SERVICE_NAME} default 2>/dev/null || true
            rm -f /etc/init.d/${SERVICE_NAME}
            ;;
        sysvinit)
            /etc/init.d/${SERVICE_NAME} stop 2>/dev/null || true
            update-rc.d -f ${SERVICE_NAME} remove 2>/dev/null || chkconfig ${SERVICE_NAME} off 2>/dev/null || true
            rm -f /etc/init.d/${SERVICE_NAME}
            ;;
    esac

    log_success "Service stopped and disabled"
}

# ==================== Uninstall ====================

uninstall_vnts() {
    log_info "Uninstalling vnts..."

    # Stop and remove service
    stop_and_disable_service

    # Remove firewall rules
    remove_firewall_rules "$DEFAULT_PORT" "$DEFAULT_WEB_PORT"

    # Remove files
    rm -rf "$INSTALL_DIR"
    rm -f "$BIN_DIR/vnts"

    log_success "vnts has been uninstalled"
}

# ==================== Status & Info ====================

show_status() {
    echo ""
    echo "=============================================="
    echo "           VNTS Installation Complete"
    echo "=============================================="
    echo ""
    echo "  Version:        v${VNTS_VERSION}"
    echo "  Install Path:   ${INSTALL_DIR}"
    echo "  Server Port:    ${SERVER_PORT} (TCP/UDP)"
    echo "  Gateway:        ${GATEWAY}"
    echo "  Netmask:        ${NETMASK}"
    echo "  Network:        ${GATEWAY%.*}.0/${NETMASK}"
    if [[ "$ENABLE_WEB" == "true" ]]; then
        echo "  Web Admin:      http://YOUR_IP:${WEB_PORT}"
        echo "  Web Credentials: admin / admin (change this!)"
    else
        echo "  Web Admin:      BLOCKED (use --web to enable)"
        echo "                  (vnts runs web on localhost:${WEB_PORT}, but firewall blocks external access)"
    fi
    echo ""
    echo "  Service Commands:"
    case $INIT_SYSTEM in
        systemd)
            echo "    Start:    systemctl start ${SERVICE_NAME}"
            echo "    Stop:     systemctl stop ${SERVICE_NAME}"
            echo "    Status:   systemctl status ${SERVICE_NAME}"
            echo "    Logs:     journalctl -u ${SERVICE_NAME} -f"
            ;;
        openrc)
            echo "    Start:    rc-service ${SERVICE_NAME} start"
            echo "    Stop:     rc-service ${SERVICE_NAME} stop"
            echo "    Status:   rc-service ${SERVICE_NAME} status"
            ;;
        sysvinit)
            echo "    Start:    /etc/init.d/${SERVICE_NAME} start"
            echo "    Stop:     /etc/init.d/${SERVICE_NAME} stop"
            echo "    Status:   /etc/init.d/${SERVICE_NAME} status"
            ;;
    esac
    echo ""
    echo "  Client Connection:"
    echo "    vnt-cli -s YOUR_SERVER_IP:${SERVER_PORT} -k YOUR_TOKEN"
    echo ""
    echo "=============================================="
}

show_help() {
    echo "VNTS Server Installation Script"
    echo ""
    echo "Usage: $0 [options]"
    echo ""
    echo "Options:"
    echo "  --port PORT        Server port (default: 29872)"
    echo "  --web-port PORT    Web admin port (default: 29870)"
    echo "  --gateway IP       Virtual network gateway (default: 10.26.0.1)"
    echo "  --netmask MASK     Virtual network netmask (default: 255.255.255.0)"
    echo "  --token TOKEN      Token whitelist (comma-separated)"
    echo "  --web              Enable web admin interface (disabled by default)"
    echo "  --uninstall        Uninstall vnts"
    echo "  --update           Update to latest version"
    echo "  -h, --help         Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0                                        # Install with defaults (10.26.0.0/24)"
    echo "  $0 --gateway 192.168.100.1               # Custom network segment"
    echo "  $0 --gateway 10.10.0.1 --netmask 255.255.0.0  # Custom /16 network"
    echo "  $0 --port 29999 --token mytoken          # Custom port and token"
    echo "  $0 --web                                  # Enable web interface"
    echo "  $0 --uninstall                            # Uninstall vnts"
    echo ""
}

# ==================== Main ====================

main() {
    # Default values
    SERVER_PORT=$DEFAULT_PORT
    WEB_PORT=$DEFAULT_WEB_PORT
    GATEWAY=$DEFAULT_GATEWAY
    NETMASK=$DEFAULT_NETMASK
    ENABLE_WEB="false"
    TOKEN=""
    ACTION="install"

    # Parse arguments
    while [[ $# -gt 0 ]]; do
        case $1 in
            --port)
                SERVER_PORT="$2"
                shift 2
                ;;
            --web-port)
                WEB_PORT="$2"
                shift 2
                ;;
            --gateway)
                GATEWAY="$2"
                shift 2
                ;;
            --netmask)
                NETMASK="$2"
                shift 2
                ;;
            --token)
                TOKEN="$2"
                shift 2
                ;;
            --web)
                ENABLE_WEB="true"
                shift
                ;;
            --uninstall)
                ACTION="uninstall"
                shift
                ;;
            --update)
                ACTION="update"
                shift
                ;;
            -h|--help)
                show_help
                exit 0
                ;;
            *)
                log_error "Unknown option: $1. Use --help for usage."
                ;;
        esac
    done

    echo ""
    echo "=============================================="
    echo "     VNTS Server Installation Script"
    echo "=============================================="
    echo ""

    # Check root
    check_root

    # Detect system
    detect_os
    detect_arch
    detect_init_system
    detect_firewall
    detect_package_manager

    # Execute action
    case $ACTION in
        install)
            install_dependencies
            get_latest_version
            download_vnts
            install_vnts
            create_service "$SERVER_PORT" "$WEB_PORT" "$ENABLE_WEB" "$TOKEN" "$GATEWAY" "$NETMASK"
            configure_firewall "$SERVER_PORT" "$WEB_PORT" "$ENABLE_WEB"
            enable_and_start_service
            show_status
            ;;
        update)
            log_info "Updating vnts..."
            stop_and_disable_service
            get_latest_version
            download_vnts
            install_vnts
            create_service "$SERVER_PORT" "$WEB_PORT" "$ENABLE_WEB" "$TOKEN" "$GATEWAY" "$NETMASK"
            enable_and_start_service
            show_status
            ;;
        uninstall)
            uninstall_vnts
            ;;
    esac
}

main "$@"
