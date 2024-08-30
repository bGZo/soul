@ECHO OFF

Powershell.exe -executionpolicy remotesigned -File  .\utils\scripts\git-profile.ps1

echo NOTE: Confirm everything signed would be corrent.
echo       The script didn't contains any operation to roll back!

pause

