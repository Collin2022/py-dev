import tkinter as tk


def create_dark_theme(root):
    # 设置全局背景色和前景色
    root.configure(bg='#333333')

    # 设置按钮的样式
    button_style = {
        'bg': '#555555',
        'fg': '#ffffff',
        'activebackground': '#777777',
        'activeforeground': '#ffffff',
        'relief': 'flat',
        'padx': 10,
        'pady': 5
    }

    # 设置标签的样式
    label_style = {
        'bg': '#333333',
        'fg': '#ffffff'
    }

    # 设置输入框的样式
    entry_style = {
        'bg': '#555555',
        'fg': '#ffffff',
        'insertbackground': '#ffffff',
        'relief': 'flat'
    }

    # 设置复选框的样式
    checkbutton_style = {
        'bg': '#333333',
        'fg': '#ffffff',
        'activebackground': '#333333',
        'activeforeground': '#ffffff',
        'selectcolor': '#555555'
    }

    # 设置单选按钮的样式
    radiobutton_style = {
        'bg': '#333333',
        'fg': '#ffffff',
        'activebackground': '#333333',
        'activeforeground': '#ffffff',
        'selectcolor': '#555555'
    }

    # 设置文本框的样式
    text_style = {
        'bg': '#555555',
        'fg': '#ffffff',
        'insertbackground': '#ffffff',
        'relief': 'flat'
    }

    return {
        'button': button_style,
        'label': label_style,
        'entry': entry_style,
        'checkbutton': checkbutton_style,
        'radiobutton': radiobutton_style,
        'text': text_style
    }


# 创建主窗口
root = tk.Tk()
root.title("Dark Theme Tkinter")
root.geometry("400x300")

# 应用暗色主题
dark_theme = create_dark_theme(root)

# 创建一些控件来测试主题
frame = tk.Frame(root, bg='#333333')
frame.pack(pady=20)

label = tk.Label(frame, text="Hello, Dark Theme!", **dark_theme['label'])
label.pack()

button = tk.Button(frame, text="Click Me", **dark_theme['button'])
button.pack(pady=10)

entry = tk.Entry(frame, **dark_theme['entry'])
entry.pack()

checkbutton = tk.Checkbutton(frame, text="Check Me", **dark_theme['checkbutton'])
checkbutton.pack()

radiobutton = tk.Radiobutton(frame, text="Option 1", **dark_theme['radiobutton'])
radiobutton.pack()

# 添加文本框控件
text = tk.Text(frame, height=5, **dark_theme['text'])
text.pack(pady=10)

# 运行主循环
root.mainloop()
