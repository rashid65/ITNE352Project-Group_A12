import tkinter as tk
from tkinter import messagebox
import socket
import json
import datetime

def create_scrollable_frame(root):
    # Create a canvas widget with a vertical scrollbar
    canvas = tk.Canvas(root)
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame inside the canvas which will hold the widgets
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Function to update the scroll region of the canvas
    def _on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame.bind("<Configure>", _on_frame_configure)

    return frame

# Detail function
def showHeadlines(fileName):                                                                         # Convers json format data into a python list & dysplays the news
    frame = create_scrollable_frame(root)

    with open(fileName, 'r') as f:                                                                          # Shows details about the news, and (if chosen) shows further details about a specific result
        results = json.load(f)
        articles = results["articles"]

        result_list = []

        for item in articles[:15]:
            result_list.append(item['source']['name'])
            result_list.append(item['author'])
            result_list.append(item['title'])

        num = 1
        formatted_results = []
        for i in range(0, len(result_list), 3):
            formatted_result = f"{num}. \n   Source: {result_list[i]}\n   Title: {result_list[i+2]}\n   Author: {result_list[i+1]}"
            formatted_results.append(formatted_result)
            num += 1
        #GUI starts here
        for widget in frame.winfo_children():
            widget.destroy()

        label = tk.Label(frame, text="Choose one Headline from the below menu to view more deatils:", font=("Arial", 14))
        label.pack(pady=10)

        selected_item = tk.IntVar()
        selected_item.set(1)  # Default to the first option

        for i, result in enumerate(formatted_results, 1):
            rbb = tk.Radiobutton(frame, text=result, variable=selected_item, value=i, font=("Arial", 12), wraplength=500)
            rbb.pack(anchor="w", padx=20, pady=10)

        submit_button = tk.Button(frame, text="Next", font=("Arial", 12), command=lambda: HeadlineDetails(selected_item.get(), articles))
        submit_button.pack(pady=10)

def HeadlineDetails(choice, articles):
    result = articles[choice - 1]

    try:
        published_datetime = datetime.datetime.strptime(result['publishedAt'], "%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        published_datetime = datetime.datetime.fromisoformat(result['publishedAt'])        
        
    publishing_date = published_datetime.date()
    publishing_time = published_datetime.time()

    for widget in root.winfo_children():
        widget.destroy()

    label = tk.Label(root, text=f"Source Name: {result['source']['name']}", font=("Arial", 14), wraplength=500)
    label.pack(anchor="w", padx=20, pady=10)
    label = tk.Label(root, text=f"Author: {result['author']}", font=("Arial", 12), wraplength=500)
    label.pack(anchor="w", padx=20, pady=10)
    label = tk.Label(root, text=f"Title: {result['title']}", font=("Arial", 12), wraplength=500)
    label.pack(anchor="w", padx=20, pady=10)
    label = tk.Label(root, text=f"URL: {result['url']}", font=("Arial", 12), wraplength=500)
    label.pack(anchor="w", padx=20, pady=10)
    label = tk.Label(root, text=f"Description: {result['description']}", font=("Arial", 12), wraplength=500)
    label.pack(anchor="w", padx=20, pady=10)
    label = tk.Label(root, text=f"Publishing Date: {publishing_date}", font=("Arial", 12), wraplength=500)
    label.pack(anchor="w", padx=20, pady=10)
    label = tk.Label(root, text=f"Publishing Time: {publishing_time}", font=("Arial", 12), wraplength=500)
    label.pack(anchor="w", padx=20, pady=10)

    quit_button = tk.Button(root, text="Quit", font=("Arial", 12), command=lambda: submit_choice(cs, "Quit", 0))
    quit_button.pack(pady=10)

def showSources(fileName):
    # Converts json format data into a python list & displays the sources
    with open(fileName, 'r') as f:
        # Shows details about the sources, and (if chosen) shows further details about a specific result
        results = json.load(f)
        sources = results["sources"]

        source_list = []

        for item in sources[:5]:
            source_list.append(item['name'])

        num = 1
        formatted_sources = []
        for i in range(0, len(source_list)):
            formatted_source = f"{num}. {source_list[i]}"
            formatted_sources.append(formatted_source)
            num += 1

        # GUI starts here
        for widget in root.winfo_children():
            widget.destroy()

        label = tk.Label(root, text="Choose one Source from the below menu to view more details:", font=("Arial", 14))
        label.pack(pady=10)

        selected_item = tk.IntVar()
        selected_item.set(1)  # Default to the first option

        for i, source in enumerate(formatted_sources, 1):
            rbb = tk.Radiobutton(root, text=source, variable=selected_item, value=i, font=("Arial", 12))
            rbb.pack(anchor=tk.W, padx=20)

        submit_button = tk.Button(root, text="Next", font=("Arial", 12), command=lambda: SourceDetails(selected_item.get(), sources))
        submit_button.pack(pady=10)

def SourceDetails(choice, sources):
    # Handle the selected number and show details
    result = sources[choice - 1]

    for widget in root.winfo_children():
        widget.destroy()

    label = tk.Label(root, text=f"Source Name: {result['name']}", font=("Arial", 14), wraplength=500)
    label.pack(pady=10)
    label = tk.Label(root, text=f"Country: {result['country']}", font=("Arial", 12), wraplength=500)
    label.pack(pady=10)
    label = tk.Label(root, text=f"Description: {result['description']}", font=("Arial", 10), wraplength=500)
    label.pack(pady=10)
    label = tk.Label(root, text=f"URL: {result['url']}", font=("Arial", 12), wraplength=500)
    label.pack(pady=10)
    label = tk.Label(root, text=f"Category: {result['category']}", font=("Arial", 12), wraplength=500)
    label.pack(pady=10)
    label = tk.Label(root, text=f"Language: {result['language']}", font=("Arial", 12), wraplength=500)
    label.pack(pady=10)

    quit_button = tk.Button(root, text="Quit", font=("Arial", 12), command=lambda: submit_choice(cs, "Quit", 0))
    quit_button.pack(pady=10)


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
    submit_button = tk.Button(root, text="Next", font=("Arial", 12), command=lambda: submit_choice(cs, selected_item.get(),1))
    submit_button.pack(pady=10)

def submit_choice(cs, choice, cases):
    if choice == "Quit": #if user quit
        cs.sendall(choice.encode('ascii'))
        root.destroy()
        return
    if cases != 3: #to not be confused with keyword
        cs.sendall(choice.encode('ascii')) # sends to the server each time it accese it
    if cases == 1:
        display_SecondMenu(choice) # moves from main menu to what the user chooses
    if cases == 2:
        Handel_Headline(choice) # moves to which option the user chose under Headlines
    if cases == 4:
        HandelSource(choice)
    
def final_Submit(type,choice,cs,woord):
    if woord:
        keyword = choice.get()
        keyword = KeywordFormat(keyword)
        cs.sendall(keyword.encode('ascii'))
    else:
        cs.sendall(choice.encode('ascii'))
    file = cs.recv(1024).decode('ascii')
    if type == "Headline":
        showHeadlines(file)
    elif type == "Source":
        showSources(file)

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

        submit_button = tk.Button(root, text="Next", font=("Arial", 12), command=lambda: submit_choice(cs, selected_item.get(),2))
        submit_button.pack(pady=10)
    
    if Menu == "List of Sources":
        label = tk.Label(root, text="Choose one option from the below menu:", font=("Arial", 14))
        label.pack(pady=10)

        choices = ["Search by category", "Search by country","Search by language","List all","Back to main menu"]
        selected_item = tk.StringVar()
        selected_item.set(choices[0])

        for choice in choices:
            rbb = tk.Radiobutton(root, text=choice, variable=selected_item, value=choice, font=("Arial", 12))
            rbb.pack(anchor=tk.W, padx=20)

        submit_button = tk.Button(root, text="Next", font=("Arial", 12), command=lambda: submit_choice(cs, selected_item.get(),4))
        submit_button.pack(pady=10)

#function to chnage the spaces into plus for the GET message
def KeywordFormat(input):
    trimmed = input.strip()
    modified = trimmed.replace(' ', '+')
    return modified

#function to handel all Headline optiions
def Handel_Headline(choice):
                                                         #keyword option
    if choice == "Search by keywords":
        for widget in root.winfo_children():
            widget.destroy()
        label = tk.Label(root, text="Please enter what you want to search for:", font=("Arial", 14))
        label.pack(pady=10)

        word = tk.Entry(root, font=("Arial", 12))
        word.pack(pady=5)

        search_button = tk.Button(root, text="Search", font=("Arial", 12), command=lambda: final_Submit("Headline",word,cs,True))
        search_button.pack(pady=10)

                                                         #category option
    if choice == "Search by category":
        for widget in root.winfo_children():
            widget.destroy()

        label = tk.Label(root, text="Choose one option from the below menu:", font=("Arial", 14))
        label.pack(pady=10)

        choices = ["business", "entertainment", "general", "health", "science", "sports", "technology"]
        selected_item = tk.StringVar()
        selected_item.set(choices[0])

        for choice in choices:
            rbb = tk.Radiobutton(root, text=choice, variable=selected_item, value=choice, font=("Arial", 12))
            rbb.pack(anchor=tk.W, padx=20)

        submit_button = tk.Button(root, text="Submit", font=("Arial", 12), command=lambda: final_Submit("Headline",selected_item.get(),cs,False))
        submit_button.pack(pady=10)
                                                            # country optin
    if choice == "Search by country":
        for widget in root.winfo_children():
            widget.destroy()

        label = tk.Label(root, text="Choose one option from the below menu:", font=("Arial", 14))
        label.pack(pady=10)

        choices = ["au","nz","ca","ae","sa","gb","us","eg","ma"]
        selected_item = tk.StringVar()
        selected_item.set(choices[0])

        for choice in choices:
            rbb = tk.Radiobutton(root, text=choice, variable=selected_item, value=choice, font=("Arial", 12))
            rbb.pack(anchor=tk.W, padx=20)

        submit_button = tk.Button(root, text="Submit", font=("Arial", 12), command=lambda: final_Submit("Headline",selected_item.get(),cs,False))
        submit_button.pack(pady=10)

                                                            #List all new headlines option
    if choice == "List all new headlines":
         for widget in root.winfo_children():
            widget.destroy()
            final_Submit("Headline",choice,cs,False)

    if choice == "Back to main menu":
        submit_choice(cs,choice,0)
        display_MainMenu()

def HandelSource(choice):
                                                    #Category option
    if choice == "Search by category":
        for widget in root.winfo_children():
            widget.destroy()

        label = tk.Label(root, text="Choose one option from the below menu:", font=("Arial", 14))
        label.pack(pady=10)

        choices = ["business", "entertainment", "general", "health", "science", "sports", "technology"]
        selected_item = tk.StringVar()
        selected_item.set(choices[0])

        for choice in choices:
            rbb = tk.Radiobutton(root, text=choice, variable=selected_item, value=choice, font=("Arial", 12))
            rbb.pack(anchor=tk.W, padx=20)

        submit_button = tk.Button(root, text="Submit", font=("Arial", 12), command=lambda: final_Submit("Source",selected_item.get(),cs,False))
        submit_button.pack(pady=10)
                                                # country option
    if choice == "Search by country":
        for widget in root.winfo_children():
            widget.destroy()

        label = tk.Label(root, text="Choose one option from the below menu:", font=("Arial", 14))
        label.pack(pady=10)

        choices = ["au","nz","ca","ae","sa","gb","us","eg","ma"]
        selected_item = tk.StringVar()
        selected_item.set(choices[0])

        for choice in choices:
            rbb = tk.Radiobutton(root, text=choice, variable=selected_item, value=choice, font=("Arial", 12))
            rbb.pack(anchor=tk.W, padx=20)

        submit_button = tk.Button(root, text="Submit", font=("Arial", 12), command=lambda: final_Submit("Source",selected_item.get(),cs,False))
        submit_button.pack(pady=10)

                                                    # Language option
    if choice == "Search by language":
        for widget in root.winfo_children():
            widget.destroy()

        label = tk.Label(root, text="Choose one option from the below menu:", font=("Arial", 14))
        label.pack(pady=10)

        choices = ["ar","en"]
        selected_item = tk.StringVar()
        selected_item.set(choices[0])

        for choice in choices:
            rbb = tk.Radiobutton(root, text=choice, variable=selected_item, value=choice, font=("Arial", 12))
            rbb.pack(anchor=tk.W, padx=20)

        submit_button = tk.Button(root, text="Submit", font=("Arial", 12), command=lambda: final_Submit("Source",selected_item.get(),cs,False))
        submit_button.pack(pady=10)

    if choice == "List all":
         for widget in root.winfo_children():
            widget.destroy()
            final_Submit("Source",choice,cs,None)

    if choice == "Back to main menu":
        submit_choice(cs,choice,0)
        display_MainMenu()

          
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cs:
    cs.connect(("127.0.0.1", 49999))
    # Create the main window
    root = tk.Tk()
    root.title("Insert Your Name")
    root.geometry("600x500")
    root.resizable(True, True)

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