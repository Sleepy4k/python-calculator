# Author: @sleepy4k
# License: MIT License
# Description: A simple calculator app with Python.
import tkinter as tk
import logic as calc

# Create a window
window = tk.Tk()

# Configure the window
CONFIG = {
    'title': 'Calculator',
    'size': (410, 500),
    'font_input': ('Arial', 30, 'bold'),
    'font_button': ('Arial', 20),
}

# Create the GUI
calc.Calculator(window, CONFIG['title'], CONFIG['size'], CONFIG['font_input'], CONFIG['font_button'])

# Run the app
if __name__ == "__main__":
    window.mainloop()
