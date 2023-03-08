# Author: @sleepy4k
# License: MIT License
# Description: A simple calculator app with Python.
from logic import *
import tkinter as tk

# Configure the window
title = "Calculator"
size = "424x400"

# Create a window
window =  tk.Tk()

# Declare Variable
tkvar = tk.StringVar(window)

# Create a frame
create_calculator_gui(tk, window, size, title, tkvar)

# Run the app
window.mainloop()