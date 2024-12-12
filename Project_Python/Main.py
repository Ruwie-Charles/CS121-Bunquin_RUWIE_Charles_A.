import tkinter as tk
from tkinter import messagebox, Canvas
import mysql.connector
from mysql.connector import Error
import subprocess


def save_to_database(user_details):
    connection = None

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ffesdb"
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create table if it doesn't exist
            create_table_query = """
            CREATE TABLE IF NOT EXISTS Users (
                ID INT AUTO_INCREMENT PRIMARY KEY,
                First_Name VARCHAR(100),
                Last_Name VARCHAR(100),
                Date_Of_Birth DATE,
                Gender ENUM('M', 'F', 'Other'),
                Age INT
            );
            """
            cursor.execute(create_table_query)

            # Insert user details
            insert_query = """
            INSERT INTO Users (First_Name, Last_Name, Date_Of_Birth, Gender, Age)
            VALUES (%s, %s, %s, %s, %s);
            """
            data = (
                user_details["first_name"],
                user_details["last_name"],
                user_details["dob"],
                user_details["gender"],
                user_details["age"]
            )
            cursor.execute(insert_query, data)
            connection.commit()
            messagebox.showinfo("Success", "User details saved successfully!")

    except Error as e:
        messagebox.showerror("Error", f"Error connecting to MySQL: {e}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


# Event handler for focus in (clear placeholder text)
def on_focus_in(entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, 'end')
        entry.config(fg='black')


# Event handler for focus out (restore placeholder text if empty)
def on_focus_out(entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.config(fg='gray')


def submit_form():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    dob = dob_entry.get()
    gender = gender_var.get()
    age = age_entry.get()

    # Validate input
    if not first_name or not last_name or not dob or not gender or not age:
        messagebox.showwarning("Validation Error", "All fields are required!")
        return

    try:
        age = int(age)
        if age <= 0 or age > 120:
            messagebox.showwarning("Validation Error", "Please enter a valid age.")
            return
    except ValueError:
        messagebox.showwarning("Validation Error", "Age must be a number.")
        return

    # Save to database
    user_details = {
        "first_name": first_name,
        "last_name": last_name,
        "dob": dob,
        "gender": gender,
        "age": age,
    }
    save_to_database(user_details)


def start_program():
    messagebox.showinfo("Next Step", "Proceeding to the main program...")

    # Use a raw string for the Windows file path
    project_path = r"C:\Users\ruwie\OneDrive\Desktop\Project_Python\Home_Page.py"

    try:
        # Close the current window before starting the new program
        root.destroy()

        # Run the Home_Page.py script using Python
        subprocess.run(['python', project_path])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to start the program: {e}")


# Function to create a gradient background
def create_gradient_background(canvas, width, height, start_color, end_color):
    r1, g1, b1 = canvas.winfo_rgb(start_color)
    r2, g2, b2 = canvas.winfo_rgb(end_color)

    r_ratio = (r2 - r1) / height
    g_ratio = (g2 - g1) / height
    b_ratio = (b2 - b1) / height

    for i in range(height):
        r = int(r1 + (r_ratio * i))
        g = int(g1 + (g_ratio * i))
        b = int(b1 + (b_ratio * i))
        color = f'#{r:04x}{g:04x}{b:04x}'
        canvas.create_line(0, i, width, i, fill=color)


# Create the main application window
root = tk.Tk()
root.title("F.F.E.S - Free Fall Educational Support")

# For window size
window_width = 500
window_height = 600

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the position for centering the window
position_top = int(screen_height / 2 - window_height / 2)
position_left = int(screen_width / 2 - window_width / 2)

# Set the window size and position
root.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")
root.resizable(False, False)

# Create a canvas to draw the gradient
canvas = Canvas(root, width=500, height=600)
canvas.pack(fill="both", expand=True)
create_gradient_background(canvas, 500, 600, "#87CEEB", "#FFFFFF")  # Gradient from sky blue to white

# Load the logo
try:
    logo_image = tk.PhotoImage(file="FFES_LOGO.png")  # Ensure the file path is correct
    canvas.create_image(150, 10, anchor="nw", image=logo_image)
except Exception as e:
    messagebox.showerror("Error", f"Failed to load logo: {e}")

# Placeholder text
dob_placeholder = "(YYYY-MM-DD)"

# Labels and entry fields
tk.Label(root, text="First Name:", fg="#003366", font=("Arial", 10, "bold")).place(x=80, y=170)
first_name_entry = tk.Entry(root, font=("Arial", 10))
first_name_entry.place(x=240, y=170, width=200)

tk.Label(root, text="Last Name:", fg="#003366", font=("Arial", 10, "bold")).place(x=80, y=220)
last_name_entry = tk.Entry(root, font=("Arial", 10))
last_name_entry.place(x=240, y=220, width=200)

tk.Label(root, text="Date of Birth:", fg="#003366", font=("Arial", 10, "bold")).place(x=80, y=270)
dob_entry = tk.Entry(root, font=("Arial", 10), fg="gray")
dob_entry.insert(0, dob_placeholder)
dob_entry.place(x=240, y=270, width=200)
dob_entry.bind("<FocusIn>", lambda event: on_focus_in(dob_entry, dob_placeholder))
dob_entry.bind("<FocusOut>", lambda event: on_focus_out(dob_entry, dob_placeholder))

tk.Label(root, text="Gender:", fg="#003366", font=("Arial", 10, "bold")).place(x=80, y=320)
gender_var = tk.StringVar()
gender_dropdown = tk.OptionMenu(root, gender_var, "M", "F", "Other")
gender_dropdown.configure(bg="#005a9e", fg="white", font=("Arial", 10))
gender_dropdown.place(x=240, y=320, width=200)

tk.Label(root, text="Age:", fg="#003366", font=("Arial", 10, "bold")).place(x=80, y=370)
age_entry = tk.Entry(root, font=("Arial", 10))
age_entry.place(x=240, y=370, width=200)

# Buttons
button_frame = tk.Frame(root)
button_frame.place(x=130, y=450)

submit_button = tk.Button(button_frame, text="Submit", command=submit_form, bg="#0073e6", fg="white", font=("Arial", 12, "bold"))
submit_button.grid(row=0, column=0, padx=10)

start_button = tk.Button(button_frame, text="Start Program", command=start_program, bg="#004080", fg="white", font=("Arial", 12, "bold"))
start_button.grid(row=0, column=1, padx=10)

# Keep a reference to the logo image
root.logo_image = logo_image

# Run the application
root.mainloop()
