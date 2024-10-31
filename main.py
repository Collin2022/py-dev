# -*- encoding: utf-8 -*-
import json
from tkinter import *
from tkinter.ttk import Combobox, Notebook
from tkinter import Text, RIGHT, BOTTOM, END
from tkinter.messagebox import *
from tkinter.filedialog import *
from os import system
from shutil import copyfile
from sys import exit

from library import theme as theme_lib

import subprocess
import platform
import re
import keyword


def open_file():
    """
    打开文件菜单函数
    :return: None
    """
    global filename
    filename = askopenfilename(
        title="py_dev", filetypes=[("Python文件", "*.py"), ("文本文件", "*.txt"), ("所有文件", "*.*")],
        initialdir=r"C:\Users\Administrator\Documents",
        defaultextension=".py"
    )
    try:
        with open(filename, "r", encoding="utf-8") as fp:
            data = fp.read()
    except FileNotFoundError:
        showerror("py_dev", "请打开文件！")
        return None
    text.insert(END, data)


def save_file():
    """
    保存文件菜单函数
    :return: None
    """
    filename = asksaveasfilename(
        title="py_dev 保存文件", filetypes=[("Python文件", "*.py"), ("文本文件", "*.txt"), ("所有文件", "*.*")],
        initialdir=r"C:\Users\Administrator\Documents",
        defaultextension=".py"
    )
    try:
        with open(filename, "w", encoding="utf-8") as fp:
            fp.write(text.get(0.0, END))
    except FileNotFoundError:
        showerror("py_dev", "请选择一个目录！")


def open_settings_file():
    """
    打开配置文件
    :return: None
    """
    _filename = askopenfilename(
        title="py_dev", filetypes=[("配置文件", "*.json")],
        initialdir=r"C:\Users\Administrator\Documents",
        defaultextension=".json"
    )

    # 复制文件
    try:
        copyfile(_filename, "./asset/database/" + _filename)
    except FileNotFoundError:
        showerror("py_dev", "请选择文件！")


def set_settings():
    """
    设置配置文件
    :return: None
    """

    def func():
        """
        设置函数
        :return: None
        """
        data[combo.get()] = entry.get()
        with open("./asset/database/settings.json", "r", encoding="utf-8") as _fp:
            json.dump(_fp, data)
        window.quit()
        showinfo("py_dev", "请重新启动软件！")
        exit()

    global data
    with open("./asset/database/settings.json", "r", encoding="utf-8") as fp:
        data = json.load(fp)

    window = Toplevel()
    window.title("设置")

    # 窗口控件
    combo = Combobox(window, values=data["key"])
    combo.grid(column=0, row=0)
    entry = Entry(window)
    entry.grid(column=1, row=0)
    button = Button(window, text="设置", command=func)
    button.grid(column=1, row=1)

    window.mainloop()  # 窗口循环


def open_settings_dir():
    """
    打开配置文件所在目录
    :return: None
    """
    system("explorer ./asset/database/settings.json")


def open_file_in_explorer(directory):
    """
    在文件资源管理器中打开dir目录
    :param directory: 目标目录
    :return: None
    """
    if platform.system() == "Windows":
        subprocess.run(["explorer", directory], shell=True)
    else:
        subprocess.run(["xdg-open", directory], shell=False)


def about():
    """
    关于
    :return: None
    """
    showinfo(
        "py_dev 版权信息",
        """
        Py_Dev
        Made with python
        Written by @Collin2022 on https://github.com/

        (c) copyright 2024-2060
        """
    )


class CodeHighlighter:
    def __init__(self, text_widget, syntax_colors):
        self.text_widget = text_widget
        self.keywords = keyword.kwlist
        self.syntax_colors = syntax_colors
        self.setup_tags()
        self.text_widget.bind("<KeyRelease>", self.delayed_highlight)

    def setup_tags(self):
        for tag, color in self.syntax_colors.items():
            self.text_widget.tag_configure(tag, foreground=color)

    def delayed_highlight(self, event=None):
        # 延迟高亮显示，以确保输入稳定
        self.text_widget.after(100, self.highlight)

    def highlight(self, event=None):
        # 清除所有标签
        for tag in self.syntax_colors.keys():
            self.text_widget.tag_remove(tag, "1.0", "end")

        # 获取文本内容
        text = self.text_widget.get("1.0", "end-1c")

        # 使用正则表达式匹配关键字、字符串、注释、数字和函数
        keyword_pattern = r"\b(" + "|".join(self.keywords) + r")\b"
        string_pattern = r"(\".*?\"|\'.*?\')"
        comment_pattern = r"#.*"
        number_pattern = r"\b\d+\b"
        function_pattern = r"\bdef\s+(\w+)\b"

        # 应用关键字标签
        for match in re.finditer(keyword_pattern, text):
            start, end = match.span()
            self.text_widget.tag_add("keyword", f"1.0+{start}c", f"1.0+{end}c")

        # 应用字符串标签
        for match in re.finditer(string_pattern, text):
            start, end = match.span()
            self.text_widget.tag_add("string", f"1.0+{start}c", f"1.0+{end}c")

        # 应用注释标签
        for match in re.finditer(comment_pattern, text):
            start, end = match.span()
            self.text_widget.tag_add("comment", f"1.0+{start}c", f"1.0+{end}c")

        # 应用数字标签
        for match in re.finditer(number_pattern, text):
            start, end = match.span()
            self.text_widget.tag_add("number", f"1.0+{start}c", f"1.0+{end}c")

        # 应用函数标签
        for match in re.finditer(function_pattern, text):
            start, end = match.span(1)
            self.text_widget.tag_add("function", f"1.0+{start}c", f"1.0+{end}c")


# 自动补齐功能
def autocomplete(event):
    char = event.char
    index = text.index("insert")

    # 自动补齐括号和引号
    if char in "([{\"\''":
        if char == "(":
            text.insert(index, "()")
        elif char == "[":
            text.insert(index, "[]")
        elif char == "{":
            text.insert(index, "{}")
        elif char == "\"":
            text.insert(index, "\"\"")
        elif char == "'":
            text.insert(index, "''")
        # 移动光标到括号或引号之间
        text.mark_set("insert", f"{index}+1c")
        return "break"  # 阻止默认输入行为


# 自动缩进功能
def auto_indent(event):
    current_line_index = text.index("insert linestart")
    current_line = text.get(current_line_index, f"{current_line_index} lineend")

    # 计算当前行的缩进空格数
    indent = len(current_line) - len(current_line.lstrip(" "))

    # 检查是否需要额外增加缩进（例如当前行以 `:` 结尾）
    if current_line.strip().endswith(":"):
        indent += 4  # 增加 4 个空格的缩进

    # 插入自动缩进的空格到新行
    text.insert("insert", "\n" + " " * indent)
    return "break"  # 阻止默认的换行行为


# 初始化窗口
root = Tk()

root.title("py_dev alpha 0.1")
root.geometry("800x600+100+200")

notebook = Notebook(root)
notebook.pack(side=TOP, expand=True, fill=BOTH)

dark_theme = theme_lib.create_dark_theme(root)

# 输出版权信息
showinfo(
    "py_dev 版权信息",
    """
    Py_Dev
    Made with python
    Written by @Collin2022 on https://github.com/

    (c) copyright 2024-2060
    """
)

# 初始化
with open("./asset/database/settings.json", "r", encoding="utf-8") as fp:
    setting = json.load(fp)

with open("./asset/database/theme/{}.json".format(setting["theme"]), "r", encoding="utf-8") as fp:
    theme = json.load(fp)

# 初始化编辑器窗口
notepad = Frame(notebook)
notebook.add(notepad, text="编辑器")

text = Text(notepad, font=("Cascadia Mono", 15), **dark_theme['text'])
text.pack(side=TOP, expand=True, fill=BOTH)
text.config(tabs=(12 * setting["tab_size"],))

# 为 Text 小部件绑定自动补齐事件
text.bind("<KeyPress>", autocomplete)
text.bind("<Return>", auto_indent)

# 语法高亮器
CodeHighlighter(text_widget=text, syntax_colors={**theme["syntax_colors"], "function": "yellow"})

# global data, filename, notepad, text

# 菜单
menu = Menu(tearoff=0)
root.config(menu=menu)

# 文件菜单
file_menu = Menu(tearoff=0)
menu.add_cascade(menu=file_menu, label="文件")  # 设置文件菜单

file_menu.add_command(command=open_file, label="打开文件")
file_menu.add_command(command=save_file, label="保存文件")
file_menu.add_command(command=save_file, label="另存为文件")
file_menu.add_separator()
file_menu.add_command(command=open_settings_file, label="打开自定义配置文件")
file_menu.add_command(command=set_settings, label="设置")
file_menu.add_command(command=open_settings_dir, label="打开配置文件所在目录")
file_menu.add_separator()
file_menu.add_separator()
file_menu.add_command(command=exit, label="退出")


# 关于菜单
menu.add_command(command=about, label="关于")

if __name__ == "__main__":
    root.mainloop()
