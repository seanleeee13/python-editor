@echo off
cd ..
pyinstaller utils\python_editor_k.spec
rmdir build /s /q
exit