import tkinter as tk
from tkinter import messagebox
import socket

def submit_name(cs):
    name = entry.get()
    if name:
        cs.sendall(name.encode('ascii'))
    else:
        messagebox.showwarning("Input Error", "Please enter your name")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cs:
    cs.connect(("127.0.0.1", 49999))
    # Create the main window
    root = tk.Tk()
    root.title("Insert Your Name")
    root.geometry("600x500")
    root.resizable(False, False)

    # Create and place the label
    label = tk.Label(root, text="Please enter your name:", font=("Arial", 14))
    label.pack(pady=10)

    # Create and place the entry widget
    entry = tk.Entry(root, font=("Arial", 12))
    entry.pack(pady=5)

    # Create and place the submit button
    submit_button = tk.Button(root, text="Submit", font=("Arial", 12), command=lambda: submit_name(cs))
    submit_button.pack(pady=10)

    # Run the application
    root.mainloop()