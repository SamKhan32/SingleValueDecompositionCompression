

import tkinter as tk
from tkinter import ttk

# Function to change button color to 'pressed' state
def on_press(event):
    button_style.configure('TButton', background='darkblue')

# Function to change button color back to 'normal' state
def on_release(event):
    button_style.configure('TButton', background='SystemButtonFace')

# Function to perform the specific action
def specific_function():
    print("Button was clicked!")

# Create main window
root = tk.Tk()
root.title("Button Color Change Example")

# Create a style object
button_style = ttk.Style()
button_style.configure('TButton', background='SystemButtonFace')

# Create a button and associate the events and command with it
button = ttk.Button(root, text="Click Me", command=specific_function)
button.grid(row=0, column=0, padx=20, pady=20)

# Bind the press and release events to the button
button.bind("<ButtonPress-1>", on_press)
button.bind("<ButtonRelease-1>", on_release)

# Start the main loop
root.mainloop()