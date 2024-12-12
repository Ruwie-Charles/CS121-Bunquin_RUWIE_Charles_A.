import mysql.connector
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import subprocess  # To run Home_Page.py

# Function to fetch data from the MySQL database
def fetch_data():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ffesdb"
        )
        cursor = conn.cursor()

        query = '''
            SELECT 
                u.User_ID, u.First_Name, u.Last_Name, u.Date_of_Birth, u.Gender, u.Age, 
                r.Result_ID, r.Problem_1, r.Problem_2, r.Problem_3, r.Score
            FROM users u
            LEFT JOIN results r ON u.User_ID = r.Result_ID
        '''
        cursor.execute(query)
        data = cursor.fetchall()
    except mysql.connector.Error as e:
        print(f"Database error: {e}")
        data = []
    finally:
        if conn.is_connected():
            conn.close()
    return data

# Function to delete a row from both users and results tables
def delete_row(user_id, result_id):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ffesdb"
        )
        cursor = conn.cursor()

        # Begin transaction
        conn.start_transaction()

        # Delete from results table
        cursor.execute('DELETE FROM results WHERE Result_ID = %s', (result_id,))

        # Delete from users table
        cursor.execute('DELETE FROM users WHERE User_ID = %s', (user_id,))

        # Commit transaction
        conn.commit()
    except mysql.connector.Error as e:
        conn.rollback()
        print(f"Error deleting row: {e}")
        messagebox.showerror("Error", "Failed to delete record. Check console for details.")
    finally:
        if conn.is_connected():
            conn.close()

# Function to handle delete button click with confirmation dialog
def on_delete():
    selected_item = treeview.selection()
    if selected_item:
        # Ask the user for confirmation before deleting
        result = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this record?")
        if result:  # User clicked 'Yes'
            item = treeview.item(selected_item)
            user_id = item['values'][0]  # The 'User_ID' of the selected row
            result_id = item['values'][6]  # The 'Result_ID' of the selected row
            delete_row(user_id, result_id)
            messagebox.showinfo("Success", "Record deleted successfully from both tables!")
            update_table()
        else:
            messagebox.showinfo("Canceled", "Record deletion was canceled.")
    else:
        messagebox.showwarning("No Selection", "Please select a row to delete.")

# Function to update the Treeview with fresh data
def update_table():
    # Clear existing rows in the Treeview
    for row in treeview.get_children():
        treeview.delete(row)
    # Fetch data and populate the Treeview
    data = fetch_data()
    for row in data:
        treeview.insert("", "end", values=row)

# Function to navigate back to the home page
def go_to_home_page():
    subprocess.Popen(["python", "Home_Page.py"])  # Launch Home_Page.py
    root.destroy()  # Close the current window

# Main GUI setup
root = tk.Tk()
root.title("Users and Results Management")

# Center and set theme
root.configure(bg="#87CEEB")
window_width = 1100
window_height = 550
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_x = (screen_width // 2) - (window_width // 2)
position_y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

# Title Label (updated placement to avoid blocking)
title_label = tk.Label(root, text="Free Fall Educational Support Database", bg="#87CEEB", fg="white",
                       font=("Arial", 20, "bold"), pady=10)
title_label.pack(side="top", pady=10)  # Ensure it stays at the top

# Treeview widget to display the database data
treeview = ttk.Treeview(root, columns=("User_ID", "First_Name", "Last_Name", "Date_of_Birth", "Gender", "Age", 
                                       "Result_ID", "Problem_1", "Problem_2", "Problem_3", "Score"), show="headings")

# Adjust column widths and text justification
column_settings = {
    "User_ID": 80, "First_Name": 100, "Last_Name": 100, "Date_of_Birth": 100,
    "Gender": 80, "Age": 60, "Result_ID": 80, "Problem_1": 100,
    "Problem_2": 100, "Problem_3": 100, "Score": 80
}
for col, width in column_settings.items():
    treeview.column(col, width=width, anchor="center")
    treeview.heading(col, text=col.replace("_", " "))

treeview.pack(padx=10, pady=10, fill="x", expand=True)

# Button Frame (move it upwards with place)
button_frame = tk.Frame(root, bg="#87CEEB")
button_frame.place(x=350, y=450)  # Adjust y value to move the frame upwards

# Add logo to the upper left with transparency blending
logo_image = tk.PhotoImage(file="FFES_LOGO.png")  # Ensure your logo supports transparency
logo_label = tk.Label(root, image=logo_image, bg="#87CEEB")  # Use same bg color as root
logo_label.place(x=10, y=10)

# Delete Button
delete_button = tk.Button(button_frame, text="Delete Selected Row", command=on_delete,
                          bg="#4682B4", fg="white", font=("Arial", 12, "bold"), relief="ridge")
delete_button.pack(side="left", padx=10)

# Back Button
back_button = tk.Button(button_frame, text="Return to Home Page", command=go_to_home_page,
                        bg="#4682B4", fg="white", font=("Arial", 12, "bold"), relief="ridge")
back_button.pack(side="left", padx=10)

# Initialize the table with existing data
update_table()

# Run the main loop
root.mainloop()
