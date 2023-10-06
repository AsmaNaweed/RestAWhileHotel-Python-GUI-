import tkinter as tk
import csv
from tkinter import messagebox

class LoginManager:
    def __init__(self):       
        self.usernameStored = ""
        self.passwordStored = ""
        self.AccountLogin = tk.Tk()  # Create a Tkinter AccountLogin window
        self.AccountLogin.title("Account Login")
        
        # Set  window size
        self.AccountLogin.geometry("400x200")
        
        # Create labels and entry widgets for username and password
        tk.Label(self.AccountLogin, text="Username:").pack()
        
        self.username_entry = tk.Entry(self.AccountLogin)
        self.username_entry.pack()
        
        tk.Label(self.AccountLogin, text="Password:").pack()
        self.password_entry = tk.Entry(self.AccountLogin, show="*")  # Use show="*" to hide the password
        self.password_entry.pack()
        
        # Create a login button
        tk.Button(self.AccountLogin, text="Login", command=self.verify_login).pack()
    
    def verify_login(self):
        # Get the username and password entered by the user
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Check if the entered credentials are valid
        if self.VerifyLogin(username, password):
            messagebox.showinfo("Login Successful")
        else:
             messagebox.showinfo("Login Filed")
        
    def VerifyLogin(self, username, password):
        with open('usernames.txt', mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                saved_username, saved_password = row
                print(saved_username + "," + saved_password)
                if username == saved_username and password == saved_password:                  
                    print("Login successful")
                    return True

        print("Invalid username or password")
        return False
    def AddLogin(self, username, password):
        self.usernameStored = username
        self.passwordStored = password

    def run(self):
        # Start the Tkinter main loop
        self.AccountLogin.mainloop()


#****************************************************************************************************************************************
#*******************************************   Password Validation  *********************************************************************

class PasswordValidator:
    def __init__(self):
        self.has_length = True
        self.has_uppercase = False
        self.has_lowercase = False
        self.has_digit = False
        self.has_blank_char = False

    def is_valid(self, password):
        self.has_length = len(password) >= 9
        self.has_uppercase = any(char.isupper() for char in password)
        self.has_lowercase = any(char.islower() for char in password)
        self.has_digit = any(char.isdigit() for char in password)
        self.has_blank_char = any(char.isspace() for char in password)

        if not self.has_length:
            print("Password should be 9 characters long.")
        if self.has_blank_char:
            print("Password cannot contain spaces.")
        if not self.has_uppercase:
            print("Password should contain at least 1 capital letter.")
        if not self.has_lowercase:
            print("Password should contain at least 1 small letter.")
        if not self.has_digit:
            print("Password should contain at least 1 digit.")
        

        return (
            self.has_length
            and not self.has_blank_char
            and self.has_uppercase
            and self.has_lowercase
            and self.has_digit
        )

def getting_input():
    validator = PasswordValidator()

    while True:
        
        password = input()
       
        if validator.is_valid(password):
            print("Password has been approved.")
            break
        else:
            print("Not a valid password.")

getting_input()

    

