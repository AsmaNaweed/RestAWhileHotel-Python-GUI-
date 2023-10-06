import tkinter as tk
from tkinter import messagebox


class CreateAccountWindow:
    def __init__(self):
        self.create_account_window = tk.Toplevel()
        self.create_account_window.title("Create Account")

        # Labels and Entry fields for username and password
        tk.Label(self.create_account_window, text="Username:").pack()
        self.username_entry = tk.Entry(self.create_account_window)
        self.username_entry.pack()

        tk.Label(self.create_account_window, text="Password (9 characters, 1 digit, 1 uppercase, 1 lowercase):").pack()
        self.password_entry = tk.Entry(self.create_account_window, show="*")
        self.password_entry.pack()

        # Button to create the account
        tk.Button(self.create_account_window, text="Create Username", command=self.create_username).pack()
        tk.Button(self.create_account_window, text="Create Password", command=self.create_password).pack()

        

#***************************************************************File for Username and Password ***********************************************

        
        
    def create_username(self):
    # Get the username entered by the user
        username = self.username_entry.get()

    try:
        # Save the username to the usernames.txt file
        with open("usernames.txt", "a") as file:
            file.write(username + "\n")

        messagebox.showinfo("Success", "Username created successfully!")
    except Exception as e:
        messagebox.showerror("Error", "Failed to save username: " + str(e))

    def create_password(self):
    # Get the password entered by the user
        password = self.password_entry.get()

    # Validate the password
    if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{9,}$', password):
        messagebox.showerror("Error", "Password must be 9 characters long and contain at least 1 digit, 1 uppercase, and 1 lowercase letter.")
    else:
        try:
            # Save the password to the passwords.txt file
            with open("passwords.txt", "a") as file:
                file.write(password + "\n")

            messagebox.showinfo("Success", "Password created successfully!")
        except Exception as e:
            messagebox.showerror("Error", "Failed to save password: " + str(e))
    def run(self):
       # Start the Tkinter main loop
         self.create_account_window.mainloop()




     
