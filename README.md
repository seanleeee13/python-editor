# python-editor v.1.1.3

This project is command prompt python editor.

## How To Use

You can download `python_editor.exe` file and use it. If you have python on your computer, you can download `python_editor.py` file and use it, too.

## Updates

While updating, I make codes on python file, and when update is finished, I make it into `.exe` file with `build.bat` file.

## File Information

- `dist/python_editor.exe`: It is `.exe` file for use.
- `docs` folder and its files: It is documents for this program.
- `src/python_editor.py`: It is a main python file.
- `src/python_editor_k.py`: It is similar with `src/python_editor.py`, but it doesn't downloads `keyboard` module. See [FAQ](#does-it-downloads-something-in-my-computer) for more information.
- `utils/build.bat`: It is file I use to make `.py` files into `exe` file.
- `utils/python_editor_k.spec`: It is a file for `pyinstaller`. See [FAQ](#what-is-spec-file) for more information.

## FAQ

### What is `.spec` file?

This file is for `pyinstaller`, a program that I use to make `.py` file into `.exe` file.

### Does it downloads something in my computer?

If you have python on your computer, yes. This program downloads `keyboard` module on your python. (only `python_editor.py` does) You can use `python_editor.exe` file or `python_editor_k.py` instead.

### I used `python_editor_k.py` file and it didn't work and it printed a message. What is happening?

```
Module 'keyboard' not found: not installed.
```

If you do not have `keyboard` module on python, it will not work.

Solutions:

1. Use `python_editor.exe` file. (Recommended)
2. Download `keyboard` module with `python -m pip install keyboard`. (If you are OK with downloading keyboard)
3. Use `python_editor.py` file. (If you are OK with downloading keyboard)

### I used `python_editor.py` and I got a message.

```
[notice] A new release of pip is available: 24.2 -> 24.3.1
[notice] To update, run: python.exe -m pip install --upgrade pip
```

You can use a command `python.exe -m pip install --upgrade pip` or use `python_editor_k.py` file or `python_editor.exe` file.

### How should I use indent? Tab key or four (two) spaces?

You can use both of it.