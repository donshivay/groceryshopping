from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import csv



loginpage = Tk()
loginpage.geometry("650x650")


def register():
    def save_credentials():
        username = username_entry.get()
        password = password_entry.get()

        # Check if username already exists
        with open("credentials.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] == username:
                    messagebox.showerror("Registration Error", "Username already exists. Please choose another.")
                    return

        # Store the credentials in the CSV file
        with open("credentials.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([username, password])

        messagebox.showinfo("Registration Successful", "Registration successful for user: {}".format(username))
        register_window.destroy()
        loginpage.destroy()
        import Main_Screen.py

    def update_strength_bar(*args):
        password = password_var.get()

        # Check password strength and set color accordingly
        if len(password) < 6:
            strength_bar.config(bg="red", text="Weak")
        elif len(password) < 10:
            strength_bar.config(bg="orange", text="Moderate")
        else:
            strength_bar.config(bg="green", text="Strong")

    global register_window
    register_window = Toplevel(loginpage)
    register_window.title("Register")
    register_window.geometry("300x200")

    Label(register_window, text="Username:").pack()
    username_entry = Entry(register_window)
    username_entry.pack()

    Label(register_window, text="Password:").pack()
    password_var = StringVar()
    password_var.trace_add("write", update_strength_bar)
    password_entry = Entry(register_window, show="*", textvariable=password_var)
    password_entry.pack()

    strength_bar = Label(register_window, text="Password Strength", bg="gray")
    strength_bar.pack()

    save_button = Button(register_window, text="Save", command=save_credentials)
    save_button.pack()

register_button = Button(loginpage, text="Register", command=register)
register_button.pack()

def login():
    def check_credentials():
        entered_username = username_entry.get()
        entered_password = password_entry.get()

        # Check if username and password match
        with open("credentials.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] == entered_username and row[1] == entered_password:
                  #if row: This condition checks if the current row is not empty. An empty row would be represented by an empty list ([]). If the row is empty, the loop continues to the next iteration.
                    messagebox.showinfo("Login Successful", "Welcome, {}".format(entered_username))
                    loginpage.destroy()
                    import Main_Screen.py
                    return

        messagebox.showerror("Login Failed", "Invalid username or password")

        username_entry.delete(0, END)
        password_entry.delete(0, END)

    global login_window
    login_window = Toplevel(loginpage)
    login_window.title("Login")
    login_window.geometry("300x150")

    Label(login_window, text="Username:").pack()
    username_entry = Entry(login_window)
    username_entry.pack()

    Label(login_window, text="Password:").pack()
    password_entry = Entry(login_window, show="*")
    password_entry.pack()

    login_button = Button(login_window, text="Login", command=check_credentials)
    login_button.pack()

loginpage.title("Main Window")

login_button = Button(loginpage, text="Login", command=login)
login_button.pack()

def back_command():
    # Destroy login_window and register_window if they exist
    if 'login_window' in globals():
        login_window.destroy()
    if 'register_window' in globals():
        register_window.destroy()

    # Destroy the main window (loginpage)
    loginpage.withdraw()

    # Unhide the root window
    import main.py

back_button = Button(loginpage, text="Back", command=back_command)
back_button.place(relx=1.0, rely=1.0, anchor=SE)

loginpage.mainloop()


#username_entry, password_entry, password_var, strength_bar:
 #   - Entry widgets for users to input their username and password.
  #  - `password_var` is a StringVar linked to the password entry for dynamic strength bar updates.
   

#`login_window` and `register_window` are declared as global variables to keep track of their existence and destroy them if needed.
