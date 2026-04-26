[Setup]
AppName=batompreto
AppVersion=1.0.0
DefaultDirName={pf}\batompreto
DefaultGroupName=batompreto
OutputDir=dist
OutputBaseFilename=batompreto-setup
Compression=lzma
SolidCompression=yes
SetupIconFile=icon.ico

[Files]
Source: "dist\batompreto.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\batompreto"; Filename: "{app}\batompreto.exe"
Name: "{commondesktop}\batompreto"; Filename: "{app}\batompreto.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a desktop shortcut"; GroupDescription: "Additional icons:"
