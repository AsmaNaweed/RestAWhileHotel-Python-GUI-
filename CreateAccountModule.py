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
        tk.Button(self.create_account_window, text="Create Account", command=self.CreateAccount).pack()        

#***************************************************************File for Username and Password ***********************************************

    def CreateAccount(self):
        # Get the username entered by the user
        username = self.username_entry.get()
        # Get the password entered by the user
        password = self.password_entry.get()
        print(username+ " " + password)
        self.AddLogin(username, password)

        
        

    
    def AddLogin(self, username, password):
        try:
        # Save the username to the usernames.txt file
            with open("usernames.txt", "a") as file:
                file.write(username + "," + password + "\n")                 #Asma,12345(pattern of the file)               
                messagebox.showinfo("Success", "Account created successfully")
        except Exception as e:
                messagebox.showerror("Error", "Failed to create account: " + str(e))

        
        
    def create_username(self):
    # Get the username entered by the user
        username = self.username_entry.get()

    
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




     
