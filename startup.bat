IF EXIST %~dp0windows GOTO INSTALLEXISTS
mkdir %~dp0windows
SET "FILENAME=%~dp0windows\miniconda.exe"
SET "URL=https://repo.continuum.io/miniconda/Miniconda2-latest-Windows-x86_64.exe"
powershell "Import-Module BitsTransfer; Start-BitsTransfer '%URL%' '%FILENAME%'"
%~dp0windows\miniconda.exe /RegisterPython=0 /AddToPath=0 /S /D=%~dp0windows\miniconda
:INSTALLEXISTS

set PATH=%~dp0windows\miniconda;%~dp0windows\miniconda\Scripts;%PATH%

python %~dp0cross_platform\git.py

python %~dp0cross_platform\packages.py
