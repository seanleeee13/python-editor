# python-editor v.1.1.2

This project is command prompt python editor.

## How To Use

You can download `python_editor.exe` file and use it. If you have python on your computer, you can download `python_editor.py` file and use it, too.

## Updates

While updating, I make codes on python file, and when update is finished, I make it into `.exe` file with `build.bat` file.

## File Information

- `dist/python_editor.exe`: It is `.exe` file for use.
- `docs` folder and its files: It is documents for this program.
- `src/python_editor.py`: It is a main python file.
- `src/python_editor_k.py`: It is similar with `src/python_editor.py`, but it doesn't downloads `keyboard` module. See FAQ for more information.
- `utils/build.bat`: It is file I use to make `.py` files into `exe` file.
- `utils/python_editor_k.spec`: It is a file for `pyinstaller`. See FAQ for more information.

## FAQ

### What is `.spec` file?

This file is for `pyinstaller`, a program that I use to make `.py` file into `.exe` file.

### Does it downloads something in my computer?

If you have python on your computer, yes. This program downloads `keyboard` module on your python. (only `python_editor.py` does)

### I don't like downloading `keyboard` module. How can I do?

You can use `python_editor.exe` file.

### I used `python_editor_k.py` file and it didn't work. What is happening?

If you do not have `keyboard` module on python, it will not work.

Solutions:

1. Use `python_editor.exe` file. (Recommanded)
2. Download `keyboard` module with `python -m pip install keyboard`. (If you are OK with downloading keyboard)
3. Use `python_editor.py` file. (If you are OK with downloading keyboard)
