# Author: @sleepy4k
# License: MIT License
# Description: A simple calculator app with Python.
import tkinter as tk
import gui
import logic

backend = logic.Logic()

# Configure the gui
numbers = "789456123"
i = 0
bttn = []
for j in range(1,4):
    for k in range(3):
        bttn.append(tk.Button(gui.frame,height =2,width=4,padx=10, pady = 10, text = numbers[i]))
        bttn[i]["bg"]= "orange"
        bttn[i].grid(row = j, column = k,padx=1,pady=1)
        bttn[i]["command"] = lambda x = numbers[i]: backend.number_press(x)
        i += 1

bttn_0 = tk.Button(gui.frame,height =2,width=4,padx=10, pady = 10, text = "0",bg="orange")
bttn_0["command"] = lambda: backend.number_press(0)
bttn_0.grid(row = 4, column = 0,  padx=1, pady = 1)

div = tk.Button(gui.frame,height =2,width=4,padx=10, pady = 10, text = "/",bg="steel blue")
div["command"] = lambda: backend.operation("divide")
div.grid(row = 1, column = 3, padx=1, pady = 1)

mult = tk.Button(gui.frame,height =2,width=4,padx=10, pady = 10, text = "*",bg="steel blue")
mult["command"] = lambda: backend.operation("times")
mult.grid(row = 2, column = 3,  padx=1, pady = 1)

minus = tk.Button(gui.frame,height =2,width=4,padx=10, pady = 10, text = "-",bg="steel blue")
minus["command"] = lambda: backend.operation("minus")
minus.grid(row = 3, column = 3, padx=1, pady = 1)

add = tk.Button(gui.frame,height =2,width=4,padx=10, pady = 10, text = "+",bg="steel blue")
add["command"] = lambda: backend.operation("add")
add.grid(row = 4, column = 3,  padx=1, pady = 1)

power = tk.Button(gui.frame, height=2,width=4,padx=10,pady=10,text="x^y",bg="green")
power["command"] = lambda: backend.operation("raise")
power.grid(row=2,column = 4,padx=1,pady=1)

rootof = tk.Button(gui.frame, height=2, width=4, padx=10, pady=10, text="y-\/x", bg = "green")
rootof["command"] = lambda: backend.operation("rootof")
rootof.grid(row=2, column=5, padx=1, pady=1)

fact = tk.Button(gui.frame, height=2, width=4, padx=10, pady=10, text="!",bg="green")
fact["command"] = lambda: backend.operation("fact")
fact.grid(row=3,column=4, padx=1, pady=1)

loge = tk.Button(gui.frame, height=2, width=4, padx=10, pady=10, text="ln",bg="green")
loge["command"] = lambda: backend.operation("ln")
loge.grid(row=3, column=5, padx=1, pady=1)

log10 = tk.Button(gui.frame, height=2, width=4, padx=10, pady=10, text="log",bg="green")
log10["command"]= lambda: backend.operation("log")
log10.grid(row=4, column=4, padx=1 , pady=1)

sine = tk.Button(gui.frame, height=2,width=4, padx=10,pady=10, text = "sin" , bg= "green")
sine["command"]=lambda: backend.operation("sine")
sine.grid(row=5,column=0,padx=1,pady=1)

cosine = tk.Button(gui.frame, height=2,width=4, padx=10,pady=10, text = "cos" , bg= "green")
cosine["command"]=lambda: backend.operation("cosine")
cosine.grid(row=5,column=1,padx=1,pady=1)

tangent = tk.Button(gui.frame, height=2,width=4, padx=10,pady=10, text = "tan" , bg= "green")
tangent["command"]=lambda: backend.operation("tangent")
tangent.grid(row=5,column=2,padx=1,pady=1)

exponent = tk.Button(gui.frame, height=2, width=4, padx=10, pady=10, text='e^x', bg="green")
exponent["command"]=lambda: backend.operation("exp")
exponent.grid(row=5,column=3,padx=1,pady=1)

inv = tk.Button(gui.frame, height=2, width=4, padx=10, pady=10, text="1/x", bg="green")
inv["command"] = lambda: backend.operation("inv")
inv.grid(row=5,column=4,padx=1,pady=1)

point = tk.Button(gui.frame,height =2,width=4,padx=10, pady = 10, text = ".",bg="white")
point["command"] = lambda: backend.number_press(".")
point.grid(row = 4, column = 1, padx=1, pady = 1)

neg= tk.Button(gui.frame,height =2,width=4,padx=10, pady = 10, text = "+/-",bg="white")
neg["command"] = backend.sign
neg.grid(row = 4, column = 2,  padx=1, pady = 1)

clear = tk.Button(gui.frame,height =2,width=4,padx=10, pady = 10, text = "C",bg="white")
clear["command"] = backend.clear
clear.grid(row = 1, column = 4,  padx=1, pady = 1)

all_clear = tk.Button(gui.frame,height =2,width=4,padx=10, pady = 10, text = "AC",bg="white")
all_clear["command"] = backend.all_clear
all_clear.grid(row = 1, column = 5, padx=1, pady = 1)

equals = tk.Button(gui.frame,height =6,width=4,padx=10, pady = 10, text = "=",bg="green")
equals["command"] = backend.sum_of_total
equals.grid(row = 4, column = 5,columnspan=1,rowspan=2,padx=1, pady = 1)

# Initialize the logic
gui.window.mainloop()
