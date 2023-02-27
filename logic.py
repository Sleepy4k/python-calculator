import gui
from tkinter import Entry
from math import factorial, sin, cos, tan, exp

text_box = Entry(gui.frame, justify="center", font="Times 16 bold", width=30)
text_box.grid(row = 0, column = 0,columnspan = 8,padx=30, pady = 30)
text_box.insert(0, "0")

class Logic():
    def __init__(self):
        self.op = ""
        self.total = 0
        self.eq = False
        self.current = ""
        self.newNumber = True
        self.opPending = False

    def number_press(self, num):
        self.eq = False
        temp = text_box.get()
        temp2 = str(num)
        if self.newNumber:
            self.current = temp2
            self.newNumber = False
        else:
            if temp2 == '.':
                if temp2 in temp:
                    return
            self.current = temp + temp2
        self.display(self.current)

    def sum_of_total(self):
        self.eq = True
        self.current = float(self.current)
        if self.opPending:
            self.do_sum()
        else:
            self.total = float(text_box.get())

    def do_sum(self):
        if self.op == "add":
            self.total += self.current
        elif self.op == "minus":
            self.total -= self.current
        elif self.op == "times":
            self.total *= self.current
        elif self.op == "divide":
            self.total /= self.current
        elif self.op == "power":
            self.total **= self.current
        elif self.op == "mod":
            self.total %= self.current
        elif self.op == "log":
            self.total = exp(self.current)
        elif self.op == "sin":
            self.total = sin(self.current)
        elif self.op == "cos":
            self.total = cos(self.current)
        elif self.op == "tan":
            self.total = tan(self.current)
        elif self.op == "fact":
            self.total = factorial(self.current)
        self.newNumber = True
        self.opPending = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.opPending:
            self.do_sum()
        elif not self.eq:
            self.total = self.current
        self.newNumber = True
        self.opPending = True
        self.op = op
        self.eq = False

    def display(self, value):
        text_box.delete(0, "end")
        text_box.insert(0, value)

    def clear(self):
        self.eq = False
        self.current = "0"
        self.display(0)
        self.newNumber = True

    def all_clear(self):
        self.clear()
        self.total = 0

    def sign(self):
        self.eq = False
        self.current = -(float(text_box.get()))
        self.display(self.current)
