pyinstaller python_editor\python_editor.spec
pyinstaller python_editor_nok\python_editor_nok.spec
rmdir build /s /q
copy dist\python_editor.exe python_editor.exe
copy dist\python_editor_nok.exe python_editor_nok.exe
rmdir dist /s /q