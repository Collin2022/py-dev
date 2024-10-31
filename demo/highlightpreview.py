import tkinter as tk

class CodeHighlighter:
    def __init__(self, text_widget):
        self.text_widget = text_widget
        self.keywords = ["def", "class", "if", "else", "elif", "for", "while", "return", "in", "not", "and", "or", "True", "False", "None"]
        self.syntax_colors = {
            "keyword": "blue",
            "string": "green",
            "comment": "gray",
            "number": "purple"
        }
        self.setup_tags()
        self.text_widget.bind("<KeyRelease>", self.highlight)

    def setup_tags(self):
        for tag, color in self.syntax_colors.items():
            self.text_widget.tag_configure(tag, foreground=color)

    def highlight(self, event=None):
        # 清除所有标签
        for tag in self.syntax_colors.keys():
            self.text_widget.tag_remove(tag, "1.0", "end")

        self.text_widget.mark_set("range_start", "1.0")
        while True:
            # Find the next match
            index = self.text_widget.search(r"\y|\Y", "range_start", stopindex="end", regexp=True)
            if not index:
                break

            # Get the matched text
            match_start = index
            match_end = f"{index}+1c"
            match_text = self.text_widget.get(match_start, match_end)

            # Determine the type of match
            if match_text in self.keywords:
                tag = "keyword"
            elif match_text.isdigit():
                tag = "number"
            elif match_text == "#":
                # Handle comments
                comment_end = self.text_widget.search("\n", match_end, stopindex="end")
                if comment_end:
                    match_end = comment_end
                else:
                    match_end = "end"
                tag = "comment"
            elif match_text in ['"', "'"]:
                # Handle strings
                string_end = self.text_widget.search(match_text, match_end, stopindex="end")
                if string_end:
                    match_end = string_end + "+1c"
                else:
                    match_end = "end"
                tag = "string"
            else:
                self.text_widget.mark_set("range_start", match_end)
                continue

            # Apply the tag
            self.text_widget.tag_add(tag, match_start, match_end)
            self.text_widget.mark_set("range_start", match_end)

# 创建主窗口
root = tk.Tk()
root.title("Code Highlighter")

# 创建Text小部件
text_widget = tk.Text(root, wrap="none")
text_widget.pack(expand=True, fill="both")

# 初始化高亮器
highlighter = CodeHighlighter(text_widget)

# 运行主循环
root.mainloop()