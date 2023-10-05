import tkinter as tk
from PIL import Image, ImageTk
from LoginModule import LoginManager
from CreateAccountModule import CreateAccountWindow

#Main Window Display

class Hotel:
    def __init__(self):        
        self.main_win = tk.Tk()
        self.main_win.title("Hotel Room Management")
        
        # Set a fixed window size (e.g., 650x250)
        self.main_win.geometry("650x250")
        
        # Make the window non-resizable
        self.main_win.resizable(False, False)

        # Configure columns if needed
        self.main_win.columnconfigure(0, minsize=50)
        self.main_win.columnconfigure(1, minsize=150)
        self.main_win.columnconfigure(2, minsize=250)
        self.main_win.columnconfigure(3, minsize=150)

    #**********************************************************************************************************************************************    

        #Creating Label of Main Window
        
        self.title_label = tk.Label(text='Hotel Management System', font=("Helvetica", 15), fg="navy")
        self.title_label.grid(row=0, column=1, columnspan=3)  # Center the label in columns 1, 2, and 3

        self.create_account_button = tk.Button(text="Create Account", width=15, font=("Helvetica", 10), command=self.create_account)
        self.create_account_button.grid(row=1, column=1, sticky="nsew")  # Position the "Create Account" button in column 1

        self.login_button = tk.Button(text="Login", width=10, font=("Helvetica", 10), command=self.login)
        self.login_button.grid(row=1, column=2, sticky="nsew")  # Position the "Login" button in column 2

        self.quit_button = tk.Button(text="Cancel", width=10, font=("Helvetica", 10), command=self.main_win.destroy)
        self.quit_button.grid(row=1, column=3, sticky="nsew")  # Position the "Cancel" button in column 3

    #***********************************************************************************************************************************************    


        # Load and display the image on main window
        
        img = Image.open(r'C:\Users\\Asma\\Desktop\\Asma.gif')
        img = img.resize((650, 250))
        img = ImageTk.PhotoImage(img)
        self.labelGIF = tk.Label(image=img)
        self.labelGIF.image = img
        self.labelGIF.place(x=50, y=60)

        tk.mainloop()

    #****************************************************************************************************************************************************
        
    #Create Account Button Module
        
    def create_account(self):
        # Replace this with the code to handle the "Create Account" button click
        print("Create Account button clicked")

        # Disable the "Create Account" button once clicked
        self.create_account_button.configure(state="disabled")

        self.create_account_window = CreateAccountWindow()
        self.create_account_window.run()
        
              




    #****************************************************************************************************************************************************
        
    #Login Button functionality
        
    def login(self):        
        # Create an instance of the LoginManager class
        login_manager_instance = LoginManager()


        self.clogin_manager_instance.configure(state="disabled")

        # Set initial username and password (you can change these)
        login_manager_instance.AddLogin("admin", "password")

        

        # Run the login manager and display the login 
        print("calling run")
        login_manager_instance.run()

  #********************************************************************************************************************************************************

Hotel_Mnagement_System = Hotel()
tk.mainloop()
