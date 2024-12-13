@echo off
pyinstaller python_editor_k.spec
rmdir build /s /q
pause > nul
exit