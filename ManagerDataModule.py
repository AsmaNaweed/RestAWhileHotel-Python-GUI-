import tkinter as tk
from tkinter import ttk

from HotelRoomReservationModule import ReserveRoomWindow



class Manager_Window:
    def __init__(self):        
        self.manager_window = tk.Toplevel()
        self.manager_window("Hotel Room Management")
        
        # Set a fixed window size (e.g., 650x250)
        self.manager_window.geometry("650x250")
        
        # Make the window non-resizable
        self.main_win.resizable(False, False)

        # Configure columns if needed
        self.manager_window.columnconfigure(0, minsize=50)
        self.manager_window.columnconfigure(1, minsize=150)
        self.manager_window.columnconfigure(2, minsize=250)
        self.manager_window.columnconfigure(3, minsize=150)

    #**********************************************************************************************************************************************    

        # Creating Labels

          #Creating Label of Main Window
        
        self.title_label = tk.Label(text='Hotel Inventory', font=("Helvetica", 15), fg="navy")
        self.title_label.grid(row=0, column=1, columnspan=3)  # Center the label in columns 1, 2, and 3

        
