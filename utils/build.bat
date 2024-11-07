@echo off
pyinstaller utils/python_editor_k.spec
rmdir build /s /q
pause > nul
exit