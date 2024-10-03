try:
    __import__("subprocess").run("python -m pip install keyboard", shell=True, stdout=__import__("subprocess").DEVNULL)
    code = []
    line = 1
    cmdpye_version = "v.1.1.1"
    print(f"Command Prompt Python Editor {cmdpye_version} (python v.{__import__("platform").python_version()})")
    print("Write 'help' for help.")
    while True:
        if len(code) < line:
            code.append("")
        try:
            __import__("keyboard").write(code[line - 1])
        except:
            raise ModuleNotFoundError("Module 'keyboard' not found: not installed.")
        line_in = input("%3d | " % line)
        if line_in == "run":
            del line
            del line_in
            del cmdpye_version
            code = "del code\n" + "\n".join(code)
            try:
                exec(code)
            except:
                __import__("traceback").print_exc()
            print("----------")
            g = __import__("copy").copy(globals())
            i = ""
            for i in ["__name__", "__doc__", "__package__", "__loader__", "__spec__", "__annotations__", "__builtins__", "__file__", "__cached__"]:
                try:
                    del g[i]
                except:
                    pass
            for i in list(g.keys()):
                exec(f"del {i}")
            try:
                del i, g
            except:
                pass
            code = []
            line = 1
            cmdpye_version = "v.1.1.1"
        elif line_in == "new":
            code = []
            line = 1
            print("----------")
        elif line_in == "line":
            temp = input("Line number, 'next' or 'prev': ")
            try:
                temp = int(temp)
            except:
                pass
            if temp == "next":
                if len(code) == line:
                    print("Line number error.")
                else:
                    line += 1
            elif temp == "prev":
                if line == 1:
                    print("Line number error.")
                else:
                    line -= 1
            elif type(temp) == int:
                temp = int(temp)
                if len(code) < temp:
                    print("Line number error.")
                else:
                    line = temp
            else:
                print("Line number error.")
            del temp
        elif line_in == "clear":
            if __import__("platform").system().lower() == "windows":
                __import__("subprocess").run("cls", shell=True)
            elif __import__("platform").system().lower() == "linux" or __import__("platform").system().lower() == "darwin":
                __import__("subprocess").run("clear", shell=True)
            print(f"Command Prompt Python Editor {cmdpye_version} (python v.{__import__("platform").python_version()})")
            print("Write 'help' for help.")
            code = []
            line = 1
        elif line_in == "cmd":
            while True:
                command = input(__import__("os").getcwd() + "> ")
                if command == "exit" or command[:5] == "exit ":
                    break
                __import__("subprocess").run(command, shell=True)
            __import__("subprocess").run("python -m pip install keyboard", shell=True, stdout=__import__("subprocess").DEVNULL)
            print("----------")
        elif line_in == "save":
            from tkinter import filedialog
            filename = filedialog.asksaveasfilename()
            del filedialog
            with open(filename, "w", encoding="utf-8") as f:
                if len(code) == line:
                    f.writelines([i + "\n" for i in code[:-1]])
                else:
                    f.writelines([i + "\n" for i in code])
            print("----------")
            code = []
            line = 1
            del filename
        elif line_in == "load":
            from tkinter import filedialog
            filename = filedialog.askopenfilename()
            del filedialog
            if filename:
                print("----------")
                with open(filename, "r", encoding="utf-8") as f:
                    code = f.readlines()
                    line = len(code) + 1
                for i, l in enumerate(code):
                    code[i] = l.strip()
                    print("%3d | %s" % (i + 1, l), end="")
            del filename
        elif line_in == "help":
            print(f"""Command Prompt Python Editor {cmdpye_version}
How to use
Write 'new' to restart coding
Write 'run' to run code
Write 'save' to save code
Write 'load' to load code
Write 'cmd' to open command prompt
Write 'clear' to clear window
Write 'help' for help
Write 'exit' to exit
----------""")
        elif line_in == "exit":
            del line_in
            break
        else:
            code[line - 1] = line_in
            line += 1
except KeyboardInterrupt:
    __import__("sys").exit()
except ModuleNotFoundError:
    __import__("sys").exit()
except Exception as e:
    print(f"Error: {e}")
    print("Please write next script with situation on https://github.com/seanleeee13/python-editor/issues/new")
    __import__("traceback").print_exc()
else:
    print("Exiting Python Editor...")