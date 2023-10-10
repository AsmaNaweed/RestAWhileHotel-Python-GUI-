import tkinter as tk
from tkinter import messagebox
import re  # Import the 're' module for regular expressions


class CreateAccountWindow:
    def __init__(self):
        print("CreateAccountWindow Constructor called.")
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
        tk.Button(self.create_account_window, text="Create Account", command=self.create_account).pack()

        

#***************************************************************File for Username and Password ***********************************************

        
        
    def is_valid_password(self, password):
        return re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{9,}$', password)

    def is_username_unique(self, username):
        with open("usernames.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                print(" line read from the file is: " + line)
                if len(line) >0:
                    print("Length of the line is " + str(len(line)))
                    existing_username, _ = line.strip().split(',')
                    if existing_username == username:
                        return False
        return True

    def create_account(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not self.is_valid_password(password):
            messagebox.showerror("Error", "Password must be 9 characters long and contain at least 1 digit, 1 uppercase, and 1 lowercase letter.")
        elif not self.is_username_unique(username):
            messagebox.showerror("Error", "Username already exists. Please choose a different username.")
        else:
            try:
                # Save the username and password as a pair to the accounts.txt file
                with open("usernames.txt", "a") as file:
                    file.write(f"{username},{password}\n")

                messagebox.showinfo("Success", "Account created successfully!")
                self.create_account_window.destroy()
            except Exception as e:
                messagebox.showerror("Error", "Failed to save account: " + str(e))

    
        
     
        

    def run(self):
       # Start the Tkinter main loop
         print("CreateAccountModule Run method called");
         self.create_account_window.mainloop()



