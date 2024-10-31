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