import tkinter as tk
import csv
from tkinter import messagebox
from HotelRoomReservationModule import ReserveRoomWindow

class LoginManager:
    def __init__(self, main_win):
        self.main_win=main_win
        self.create_account_window=tk.Toplevel()
        self.create_account_window.title("Create Account")
        print("Login Manager Constructor");  
        self.usernameStored = ""
        self.passwordStored = ""
        self.AccountLogin = tk.Toplevel()  # Create a Tkinter AccountLogin window
        self.AccountLogin.title("Account Login")
        
        # Set window size
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
        # Get the entered username and password
        username = self.username_entry.get()
        password = self.password_entry.get()

        with open('usernames.txt', mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if len(row) >= 2:
                    saved_username, saved_password = row
                    if username == saved_username and password == saved_password:
                        messagebox.showinfo("Login Successful", "Account login successful.")
                         # Close the login window
                        print("About to destroy the login window")
                        self.AccountLogin.destroy()
                         # Open a new window upon successful login
                        self.Display_Reserve_Room_Window(username)
                       
                        
                        return

        messagebox.showerror("Login Failed", "Invalid username or password")


       
    def AddLogin(self, username, password):
        self.usernameStored = username
        self.passwordStored = password

    def Display_Reserve_Room_Window(self, username):
          self.ReservationWindow=ReserveRoomWindow(username)
                       
    def run(self):
        # Start the Tkinter main loop
        self.AccountLogin.mainloop()






        

        
