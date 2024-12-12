import tkinter as tk
from tkinter import messagebox
import subprocess

def handle_choice(choice, root):
    root.destroy()

    if choice == 1:
        messagebox.showinfo("Navigate", "Entering to Learn Free Fall.")
        subprocess.run(["python", r"LrnFreeFall.py"])
    elif choice == 2:
        messagebox.showinfo("Navigate", "Entering how to solve Free Fall.")
        subprocess.run(["python", r"HTSFreeFall.py"])
    elif choice == 3:
        messagebox.showinfo("Navigate", "Entering Problem Solving.")
        subprocess.run(["python", r"Problem.py"])
    elif choice == 4:
        messagebox.showinfo("Navigate", "Entering to check data.")
        subprocess.run(["python", r"Data.py"])
    else:
        messagebox.showerror("Error", "The selected option is not valid.")

def home_gui():
    root = tk.Tk()
    root.title("Free Fall Educational Support Home Page")
    
    # Updated window size
    window_width = 500
    window_height = 500  # Increased window height for better layout

    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the position for centering the window
    position_top = int(screen_height / 2 - window_height / 2)
    position_left = int(screen_width / 2 - window_width / 2)

    # Set the window size and position
    root.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")
    
    root.resizable(False, False)
    
    bg_color = "#87CEEB"
    root.configure(bg=bg_color)

    # Logo
    logo_image = tk.PhotoImage(file="FFES_LOGO.png") 
    logo_label = tk.Label(root, image=logo_image, bg=bg_color)
    logo_label.place(x=150, y=10)

    # Menu options
    menu_frame = tk.Frame(root, bg=bg_color)
    menu_frame.place(x=100, y=180)  # Moved buttons further down for better spacing

    options = [
        ("Learn about Free Fall", 1),
        ("Learn how to solve Free Fall", 2),
        ("Try some problems", 3),
        ("Check your data", 4),
    ]

    for text, value in options:
        tk.Button(
            menu_frame,
            text=text,
            font=("Arial", 12),
            width=30,
            bg="white",
            fg="#333333",
            relief="raised",
            bd=3,
            activebackground="#ADD8E6", 
            activeforeground="#333333",
            command=lambda val=value: handle_choice(val, root),
        ).pack(pady=10)  # Increased padding between buttons

    # Exit button for the home page
    tk.Button(
        root,
        text="Exit",
        font=("Arial", 12),
        bg="white",
        fg="#333333",
        relief="raised",
        bd=3,
        activebackground="#ADD8E6",
        activeforeground="#333333",
        command=root.quit,
    ).place(x=220, y=420)  # Positioned the exit button at the bottom center

    root.mainloop()


if __name__ == "__main__":
    home_gui()
