import tkinter as tk
import random

def move_no_button(event=None):
    x = random.randint(0, 300)
    y = random.randint(0, 300)
    no_button.place(x=x, y=y)

def show_text():
    label.config(text="You're correct!❤")

root = tk.Tk()
root.title("Button Example")
root.geometry('1080x720')

# Label at the center
label = tk.Label(root, text="Do someone's care?", font=("Arial", 12))
label.pack(pady=20)

# Yes button
yes_button = tk.Button(root, text="Yes", command=show_text)
yes_button.pack(pady=5)

# No button
no_button = tk.Button(root, text="No", command=move_no_button)
no_button.pack(pady=5)

# Binding the hover event to the No button
no_button.bind("<Enter>", move_no_button)

root.mainloop()
