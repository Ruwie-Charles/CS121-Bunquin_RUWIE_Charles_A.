import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import subprocess

# Function to save the results to the database
def save_to_database(results):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ffesdb"
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Insert the results into the table
            query = """
            INSERT INTO results (Problem_1, Problem_2, Problem_3, Score)
            VALUES (%s, %s, %s, %s);
            """
            data = (results["ans1"], results["ans2"], results["ans3"], results["score"])
            cursor.execute(query, data)
            connection.commit()
            messagebox.showinfo("Database", "Results saved successfully!")

    except Error as e:
        messagebox.showerror("Database Error", f"Error connecting to MySQL: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

# Function to evaluate answers
def evaluate_answers(answers, root):
    correct_answers = {"problem1": 49, "problem2": 122.5, "problem3": 30.63}
    score = 0
    results = {}

    # Evaluate each answer
    results["ans1"] = "Correct" if answers[0] == correct_answers["problem1"] else "Wrong"
    if results["ans1"] == "Correct": score += 1

    results["ans2"] = "Correct" if answers[1] == correct_answers["problem2"] else "Wrong"
    if results["ans2"] == "Correct": score += 1

    results["ans3"] = "Correct" if answers[2] == correct_answers["problem3"] else "Wrong"
    if results["ans3"] == "Correct": score += 1

    results["score"] = score

    # Display the results in a popup
    result_message = (
        f"Problem 1: {results['ans1']}\n"
        f"Problem 2: {results['ans2']}\n"
        f"Problem 3: {results['ans3']}\n\n"
        f"Your total score: {score}/3"
    )
    messagebox.showinfo("Results", result_message)

    # Save results to the database
    save_to_database(results)

    # Navigate back to Home_Page.py after submitting results
    go_to_home_page()

# Function to go back to the home page
def go_to_home_page():
    subprocess.Popen(["python", "Home_Page.py"]) 
    root.destroy()

# Event handler for focus in (clear placeholder text)
def on_focus_in(entry):
    if entry.get() == "0.0":  # If the placeholder text is shown
        entry.delete(0, 'end')  # Clear it

# Event handler for focus out (restore placeholder text if empty)
def on_focus_out(entry):
    if entry.get() == "":  # If the entry is empty
        entry.insert(0, "0.0")  # Restore the placeholder text

# GUI-based problem-solving function
def problem_gui():
    global root
    root = tk.Tk()
    root.title("Free Fall Sample Problem")
    root.geometry("700x600")
    root.resizable(False, False)
    root.configure(bg="#87CEEB")

    # Center the window on the screen
    window_width = 700
    window_height = 600  
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_x = (screen_width // 2) - (window_width // 2)
    position_y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

    # Display the logo
    logo_image = tk.PhotoImage(file="FFES_LOGO.png")
    logo_label = tk.Label(root, image=logo_image, bg="#87CEEB")
    logo_label.place(x=10, y=18, relheight=0.25)

    # Title label
    title_label = tk.Label(root, text="Free Fall Sample Problem", font=("Arial", 18, "bold"), bg="#87CEEB", fg="black")
    title_label.pack(pady=(90, 20))

    # Answer variables
    answers = [tk.DoubleVar(), tk.DoubleVar(), tk.DoubleVar()]

    # Default placeholder value
    default_value = "0.0"

    # Problem content
    problems = [
        ("1. Velocity After Falling\n\n"
         "An object is dropped from rest. What is its velocity after 5 seconds?\n\n"
         "Formula: v = u + gt\nGiven:\n  u = 0 m/s\n  g = 9.8 m/s²\n  t = 5 s\n\n"
         "The velocity after 5 seconds is ___ m/s", answers[0]),
        ("2. Distance Fallen\n\n"
         "How far does the object fall in 5 seconds?\n\n"
         "Formula: h = ut + 1/2 gt²\nGiven:\n  u = 0 m/s\n  g = 9.8 m/s²\n  t = 5 s\n\n"
         "The object falls ___ m", answers[1]),
        ("3. Height Given Final Velocity\n\n"
         "An object hits the ground with a velocity of 24.5 m/s. From what height was it dropped?\n\n"
         "Formula: h = (v² - u²) / (2g)\nGiven:\n  v = 24.5 m/s\n  u = 0 m/s\n  g = 9.8 m/s²\n\n"
         "The object was dropped from a height of ___ m", answers[2]),
    ]

    # Function to display each problem
    def display_problem(index):
        for widget in frame.winfo_children():
            widget.destroy()

        # Display the problem text
        problem_label = tk.Label(
            frame, text=problems[index][0], font=("Arial", 12), wraplength=600, justify="left", bg="#87CEEB"
        )
        problem_label.pack(pady=10)

        # Input field for the answer
        tk.Label(frame, text="Your Answer:", bg="#87CEEB").pack()
        entry = tk.Entry(frame, textvariable=problems[index][1], font=("Arial", 12), fg="black")
        entry.delete(0, tk.END)  # Clear any existing text (if any)
        entry.insert(0, default_value)  # Insert the corrected placeholder text "0.0"
        entry.pack(pady=5)

        # Bind the focus events to the entry field
        entry.bind("<FocusIn>", lambda event, entry=entry: on_focus_in(entry))
        entry.bind("<FocusOut>", lambda event, entry=entry: on_focus_out(entry))

        # Navigation buttons
        nav_frame = tk.Frame(frame, bg="#87CEEB")
        nav_frame.pack(pady=10)

        # Button style
        button_style = {"bg": "#4682B4", "fg": "white", "font": ("Arial", 10, "bold"), "relief": "ridge"}

        # Back button to go to home page
        tk.Button(nav_frame, text="Back", command=go_to_home_page, **button_style).pack(side="left", padx=5)

        if index > 0:
            tk.Button(nav_frame, text="Previous", command=lambda: display_problem(index - 1), **button_style).pack(side="left", padx=5)
        if index < len(problems) - 1:
            tk.Button(nav_frame, text="Next", command=lambda: display_problem(index + 1), **button_style).pack(side="left", padx=5)
        else:
            tk.Button(nav_frame, text="Submit", command=lambda: evaluate_answers([a.get() for a in answers], root), **button_style).pack(side="left", padx=5)

    # Main content frame
    frame = tk.Frame(root, bg="#87CEEB")
    frame.pack(expand=True, fill="both", padx=10, pady=10)

    # Display the first problem
    display_problem(0)

    root.mainloop()

if __name__ == "__main__":
    problem_gui()
