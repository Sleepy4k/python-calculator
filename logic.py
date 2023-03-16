# Author: @sleepy4k
# License: MIT License
# Description: A simple calculator app with Python.
from tkinter import Button, Entry, Frame, StringVar

class Calculator:
    def __init__(self, root, title, size, font_input, font_button):
        self.expression = ""
        self.input_text = StringVar()
        self.allowed_buttons = [
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
            ".", "+", "-", "*", "/", "(", ")", "C", "<-", "="
        ]
        self.root = root
        self.root.geometry(f"{size[0]}x{size[1]}")
        self.root.resizable(0, 0)
        self.root.title(title)
        self.bind_buttons()
        self.create_gui(font_input, font_button)

    def bind_buttons(self):
        for button in self.allowed_buttons:
            if button == "C":
                self.root.bind("<Escape>", lambda event: self.clear())
                self.root.bind("<Delete>", lambda event: self.clear())
            elif button == "<-":
                self.root.bind("<BackSpace>", lambda event: self.delete())
            elif button == "=":
                self.root.bind("<Return>", lambda event: self.calculate())
            else:
                self.root.bind(button, lambda event, btn=button: self.click(btn))

    def create_gui(self, font_input, font_button):
        input_frame = Frame(self.root, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        input_frame.pack(side="top")

        input_field = Entry(input_frame, font=font_input, textvariable=self.input_text, width=50, bg="#eee", bd=0, justify="right")
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

        btns_frame = Frame(self.root, width=312, height=272.5, bg="grey")
        btns_frame.pack()

        row = 1
        col = 0

        for button in self.allowed_buttons:
            btn = Button(btns_frame, text=button, font=font_button, fg="black", width=6, height=2, bd=0, bg="#fff", cursor="hand2")

            self.root.rowconfigure(row, weight=1)
            self.root.columnconfigure(col, weight=1)

            if button == "(":
                btn.configure(command=lambda btn=button: self.click(btn))
                btn.grid(row=0, column=0, padx=1, pady=1)
            elif button == ")":
                btn.configure(command=lambda btn=button: self.click(btn))
                btn.grid(row=0, column=1, padx=1, pady=1)
            elif button == "C":
                btn.configure(command=self.clear)
                btn.grid(row=0, column=2, padx=1, pady=1)
            elif button == "<-":
                btn.configure(command=self.delete)
                btn.grid(row=0, column=3, padx=1, pady=1)
            elif button == "=":
                btn.configure(command=self.calculate)
                btn.grid(row=4, column=3, padx=1, pady=1)
            else:
                btn.configure(command=lambda btn=button: self.click(btn))
                btn.grid(row=row, column=col, padx=1, pady=1)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def click(self, btn):
        self.expression += str(btn)
        self.input_text.set(self.expression)

    def clear(self):
        self.expression = ""
        self.input_text.set("")

    def delete(self):
        self.expression = self.expression[:-1]
        self.input_text.set(self.expression)

    def calculate(self):
        try:
            self.expression = str(eval(self.expression))
        except ZeroDivisionError:
            self.expression = "0"
        self.input_text.set(self.expression)
