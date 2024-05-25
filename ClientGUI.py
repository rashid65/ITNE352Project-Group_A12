import tkinter as tk
from tkinter import messagebox
import socket

def submit_name(cs):
    name = entry.get()
    if name:
        cs.sendall(name.encode('ascii'))
        display_MainMenu()
    else:
        messagebox.showwarning("Input Error", "Please enter your name")

def display_MainMenu():
    # Clear the window
    for widget in root.winfo_children():
        widget.destroy()

    # Display the new message
    label = tk.Label(root, text="Choose one option from the below menu:", font=("Arial", 14))
    label.pack(pady=10)

    # Create and place the radio buttons for the menu items
    choices = ["Search Headlines", "List of Sources", "Quit"]
    selected_item = tk.StringVar()
    selected_item.set(choices[0])  # Default choice

    for choice in choices:
        rb = tk.Radiobutton(root, text=choice, variable=selected_item, value=choice, font=("Arial", 12))
        rb.pack(anchor=tk.W, padx=20)

    # Create and place the submit button for the menu
    submit_button = tk.Button(root, text="Submit", font=("Arial", 12), command=lambda: submit_choice(cs, selected_item.get()))
    submit_button.pack(pady=10)

def submit_choice(cs, choice):
    cs.sendall(choice.encode('ascii'))
    display_SecondMenu(choice)

def display_SecondMenu(Menu):
    for widget in root.winfo_children():
        widget.destroy()
    
    if Menu == "Search Headlines":
        label = tk.Label(root, text="Choose one option from the below menu:", font=("Arial", 14))
        label.pack(pady=10)

        choices = ["Search by keywords", "Search by category", "Search by country","List all new headlines","Back to main menu"]
        selected_item = tk.StringVar()
        selected_item.set(choices[0])

        for choice in choices:
            rbb = tk.Radiobutton(root, text=choice, variable=selected_item, value=choice, font=("Arial", 12))
            rbb.pack(anchor=tk.W, padx=20)

        submit_button = tk.Button(root, text="Submit", font=("Arial", 12), command=lambda: submit_choice(cs, selected_item.get()))
        submit_button.pack(pady=10)
        
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