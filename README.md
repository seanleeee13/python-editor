# python-editor v.0.0.1

This project is command prompt python editor.

## How to use

You can download `python_editor/python_editor.exe` file and use it. If you have python on your computer, you can download `python_editor/python_editor.py` file and use it, too.

## Updates

While updating, I make codes on python file, and when update is finished, I make it into .exe file with `build.bat` file.

## FAQ

### What is .spec files?

This file is for pyinstaller, a program that I use to make .py file into .exe file.

### Does it downloads something in my computer?

If you have python on your computer, yes. This program downloads `keyboard` module on your python.

### I don`t like downloading `keyboard` module. How can I do?

You can use `python_editor_nok/python_editor_nok.py` file and `python_editor_nok/python_editor_nok.exe` file.

### I used `python_editor_nok.py` file and it didn`t work. What is happening?

If you do not have `keyboard` module on python, it will not work.

Solutions:

1. Use `python_editor_nok/python_editor_nok.exe` file.
2. Download `keyboard` module with `python -m pip install keyboard`.
3. Use `python_editor/python_editor.py` file and `python_editor/python_editor.exe` file. (downloads `keyboard` module on your computer)