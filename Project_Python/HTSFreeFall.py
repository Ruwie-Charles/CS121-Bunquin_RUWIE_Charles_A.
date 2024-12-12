import tkinter as tk
from tkinter import ttk
import os


def on_back():
    root.destroy()
    os.system("python Home_Page.py")


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    window.geometry(f"{width}x{height}+{x}+{y}")


def display_htgs_gui():
    global root
    root = tk.Tk()
    root.title("How to Solve Free Fall Problems")

    # Increase window size
    window_width = 800
    window_height = 770
    center_window(root, window_width, window_height)
    root.resizable(False, False)

    sky_color = "#87CEEB"
    root.configure(bg=sky_color)

    # Load and place the logo image
    logo_image = tk.PhotoImage(file="FFES_LOGO.png")
    logo_label = tk.Label(root, image=logo_image, bg=sky_color)
    logo_label.place(x=10, y=10)

    # Back button
    back_button = tk.Button(
        root,
        text="Back",
        font=("Arial", 12, "bold"),
        bg="light blue",
        fg="black",
        relief="raised",
        activebackground="#ADD8E6",
        activeforeground="black",
        command=on_back,
    )
    back_button.place(relx=0.45, rely=0.93)  # Adjusted to keep it at the bottom

    # Title
    title = tk.Label(
        root,
        text="How To Solve Free Fall Problems",
        font=("Arial", 20, "bold"),
        bg=sky_color,
        fg="white",
    )
    title.place(relx=0.25, y=80)  # Adjusted position to move it to the right and down

    # Container frame for content
    container = tk.Frame(root, bg=sky_color, padx=10, pady=10)
    container.place(relx=0.05, rely=0.21, relwidth=0.9, relheight=0.7)  # Positioned lower

    # Content frame
    content_frame = tk.Frame(container, bg=sky_color)
    content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Scrollable text area
    scrollbar = ttk.Scrollbar(content_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    text_area = tk.Text(
        content_frame,
        wrap=tk.WORD,
        font=("Arial", 12),
        bg="#E0F7FA",
        fg="black",
        yscrollcommand=scrollbar.set,
        highlightthickness=0,
    )
    text_area.pack(fill=tk.BOTH, expand=True)

    scrollbar.config(command=text_area.yview)

    # Content text
    content = (
        "Welcome to How To Solve Free Fall Problems!\n\n"
        "Free-Fall Acceleration\n"
        "- Consider a ball thrown up into the air:\n"
        "  - Moving upward: velocity decreases, acceleration is 9.8 m/s².\n"
        "  - Top of path: velocity is zero, acceleration is –9.8 m/s².\n"
        "  - Moving downward: velocity increases, acceleration is –9.8 m/s².\n\n"
        "FORMULAS\n\n"
        "1. Velocity of a Falling Object:\n"
        "\tv = u + gt\n"
        "Where:\n"
        "\t - v: Final velocity (m/s).\n"
        "\t - u: Initial velocity (m/s).\n"
        "\t - g: Acceleration due to gravity (9.8 m/s²).\n"
        "\t - t: Time of fall (s).\n\n"
        "2. Distance Fallen:\n"
        "\th = ut + 1/2 gt²\n"
        "Where:\n"
        "\t - h: Height or distance fallen (m).\n"
        "\t - u: Initial velocity (m/s).\n"
        "\t - g: Acceleration due to gravity (9.8 m/s²).\n"
        "\t - t: Time of fall (s).\n\n"
        "3. Final Velocity (No Time Given):\n"
        "\tv² = u² + 2gh\n"
        "Where:\n"
        "\t - v: Final velocity (m/s).\n"
        "\t - u: Initial velocity (m/s).\n"
        "\t - g: Acceleration due to gravity (9.8 m/s²).\n"
        "\t - h: Height or distance fallen (m).\n\n"
        "EXAMPLES\n\n"
        "Example 1: Velocity After Falling for 3 Seconds\n"
        "\nProblem: An object is dropped from rest. What is its velocity after 3 seconds?\n"
        "\nSolution: Use the formula: v = u + gt\n"
        "Given:\n"
        "\t - u = 0 m/s (dropped from rest).\n"
        "\t - g = 9.8 m/s².\n"
        "\t - t = 3 s.\n"
        "Answer: The velocity after 3 seconds is 29.4 m/s.\n\n"
        "Example 2: Distance Fallen After 3 Seconds\n"
        "\nProblem: How far has the object fallen after 3 seconds?\n"
        "\nSolution: Use the formula: h = ut + 1/2 gt²\n"
        "Given:\n"
        "\t - u = 0 m/s.\n"
        "\t - g = 9.8 m/s².\n"
        "\t - t = 3 s.\n"
        "Answer: The object has fallen 44.1 m after 3 seconds.\n\n"
        "Example 3: Height of Fall Given Final Velocity\n"
        "\nProblem: An object hits the ground with a velocity of 19.6 m/s. From what height was it dropped?\n"
        "\nSolution: Use the formula: v² = u² + 2gh\n"
        "\nRearrange to solve for h: h = (v² - u²) / (2g)\n"
        "Given:\n"
        "\t - v = 19.6 m/s.\n"
        "\t - u = 0 m/s (dropped from rest).\n"
        "\t - g = 9.8 m/s².\n"
        "Answer: The object was dropped from a height of 19.6 m.\n"
    )
    text_area.insert(tk.END, content)
    text_area.configure(state=tk.DISABLED)

    root.mainloop()


if __name__ == "__main__":
    display_htgs_gui()
