import tkinter as tk
from tkinter import messagebox
import subprocess

def go_back():
    """Navigate back to the home page and close the current window."""
    try:
        root.destroy()
        subprocess.Popen(["python", "Home_Page.py"])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to navigate to Home Page: {e}")

def create_gradient(canvas, width, height, start_color, end_color):
    """Create a gradient background using a transition from start_color to end_color."""
    r1, g1, b1 = canvas.winfo_rgb(start_color)
    r2, g2, b2 = canvas.winfo_rgb(end_color)

    # Convert to range 0-255
    r1, g1, b1 = r1 // 256, g1 // 256, b1 // 256
    r2, g2, b2 = r2 // 256, g2 // 256, b2 // 256

    r_ratio = (r2 - r1) / height
    g_ratio = (g2 - g1) / height
    b_ratio = (b2 - b1) / height

    for i in range(height):
        r = int(r1 + (r_ratio * i))
        g = int(g1 + (g_ratio * i))
        b = int(b1 + (b_ratio * i))
        color = f'#{r:02x}{g:02x}{b:02x}'
        canvas.create_line(0, i, width, i, fill=color)

def display_info_gui():
    global root 
    root = tk.Tk()
    root.title("Learn About Free Fall")

    # Set window size
    window_width = 650
    window_height = 500

    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate position to center the window
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)

    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
    root.resizable(False, False)

    # Create a canvas to draw the gradient background
    canvas = tk.Canvas(root, width=window_width, height=window_height, highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)

    # Call create_gradient to create a smooth gradient
    create_gradient(canvas, window_width, window_height, 'deepskyblue', 'skyblue')

    # Add logo to the upper left
    logo_image = tk.PhotoImage(file="FFES_LOGO.png")
    logo_label = tk.Label(root, image=logo_image, bg="deepskyblue")
    logo_label.place(x=10, y=10)

    # Add a title on top of the gradient
    title = tk.Label(
        root,
        text="LET'S TRY AND LEARN ABOUT FREE FALL",
        font=("Arial", 16, "bold"),
        bg="deepskyblue",
        fg="black",
        pady=10
    )
    title.place(x=170, y=50)  # Adjusted to avoid overlap with the logo

    # Add information text
    info_text = (
        "FREE FALL\n"
        "- Free fall is the motion of a body when only the force due to gravity is acting on the body.\n"
        "- The acceleration on an object in free fall is called the acceleration due to gravity, or free-fall acceleration.\n"
        "- Free-fall acceleration is denoted with the symbols 'ag' (generally) or 'g' (on Earth’s surface).\n\n"
        "FREE-FALL ACCELERATION\n"
        "- Free-fall acceleration is the same for all objects, regardless of mass.\n"
        "- We use the value g = 9.81 m/s².\n"
        "- Free-fall acceleration on Earth’s surface is –9.81 m/s² at all points in the object’s motion."
    )

    content_frame = tk.Frame(root, bg="skyblue")
    content_frame.place(relx = 0.5, rely = 0.6, anchor="center", width=550, height=270)

    content = tk.Label(
        content_frame,
        text=info_text,
        font=("Arial", 12),
        fg="black",
        justify=tk.LEFT,
        wraplength=520,
        bg="skyblue"
    )
    content.pack(padx=10, pady=10)

    # Add a back button
    back_button = tk.Button(
        root,
        text="BACK",
        font=("Arial", 12, "bold"),
        bg="light blue",
        fg="black",
        command=go_back,
        padx=10,
        pady=5
    )
    back_button.place(relx=0.5, rely=0.9, anchor="center")

    root.mainloop()

if __name__ == "__main__":
    display_info_gui()
