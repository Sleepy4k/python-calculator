def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_delete():
    global expression
    result = str(expression)[:-1]
    input_text.set(result)
    expression = result

def btn_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = result

def btn_bind(root):
    root.bind("<Return>", lambda event: btn_equal())
    root.bind("<BackSpace>", lambda event: btn_delete())
    root.bind("<Escape>", lambda event: btn_clear())
    root.bind("<Delete>", lambda event: btn_clear())
    root.bind("9", lambda event: btn_click(9))
    root.bind("8", lambda event: btn_click(8))
    root.bind("7", lambda event: btn_click(7))
    root.bind("6", lambda event: btn_click(6))
    root.bind("5", lambda event: btn_click(5))
    root.bind("4", lambda event: btn_click(4))
    root.bind("3", lambda event: btn_click(3))
    root.bind("2", lambda event: btn_click(2))
    root.bind("1", lambda event: btn_click(1))
    root.bind("0", lambda event: btn_click(0))
    root.bind(".", lambda event: btn_click("."))
    root.bind("+", lambda event: btn_click("+"))
    root.bind("-", lambda event: btn_click("-"))
    root.bind("*", lambda event: btn_click("*"))
    root.bind("/", lambda event: btn_click("/"))

expression = ""
input_text = ""

def create_calculator_gui(tk, root, size, title, input, font_input, font_button):
    global input_text
    input_text = input

    root.geometry(size)
    root.resizable(0, 0)
    root.title(title)

    btn_bind(root)

    input_frame = tk.Frame(root, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
    input_frame.pack(side = tk.TOP)

    input_field = tk.Entry(input_frame, font=font_input, textvariable=input_text, width=50, bg="#eee", bd=0, justify = tk.RIGHT)
    input_field.grid(row=0, column=0)
    input_field.pack(ipady=10)

    btns_frame = tk.Frame(root, width=312, height=272.5, bg="grey")
    btns_frame.pack()

    clear = tk.Button(btns_frame, text="Clear", font=font_button, fg="black", width=13, height=2, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_clear()).grid(row=0, column=0, columnspan=2, padx=1, pady=1)
    delete = tk.Button(btns_frame, text="Delete", font=font_button, fg="black", width=6, height=2, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_delete()).grid(row=0, column=2, padx=1, pady=1)
    divide = tk.Button(btns_frame, text="/", font=font_button, fg="black", width=6, height=2, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click("/")).grid(row=0, column=3, padx=1, pady=1)

    seven = tk.Button(btns_frame, text="7", font=font_button, fg="black", width=6, height=2, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)
    eight = tk.Button(btns_frame, text="8", font=font_button, fg="black", width=6, height=2, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)
    nine = tk.Button(btns_frame, text="9", font=font_button, fg="black", width=6, height=2, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)
    multiply = tk.Button(btns_frame, text = "*", font=font_button, fg = "black", width = 6, height = 2, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)

    four = tk.Button(btns_frame, text = "4", font=font_button, fg = "black", width = 6, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
    five = tk.Button(btns_frame, text = "5", font=font_button, fg = "black", width = 6, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
    six = tk.Button(btns_frame, text = "6", font=font_button, fg = "black", width = 6, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
    minus = tk.Button(btns_frame, text = "-", font=font_button, fg = "black", width = 6, height = 2, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)

    one = tk.Button(btns_frame, text = "1", font=font_button, fg = "black", width = 6, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
    two = tk.Button(btns_frame, text = "2", font=font_button, fg = "black", width = 6, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
    three = tk.Button(btns_frame, text = "3", font=font_button, fg = "black", width = 6, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
    plus = tk.Button(btns_frame, text = "+", font=font_button, fg = "black", width = 6, height = 2, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)

    zero = tk.Button(btns_frame, text = "0", font=font_button, fg = "black", width = 13, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
    point = tk.Button(btns_frame, text = ".", font=font_button, fg = "black", width = 6, height = 2, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
    equals = tk.Button(btns_frame, text = "=", font=font_button, fg = "black", width = 6, height = 2, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)
