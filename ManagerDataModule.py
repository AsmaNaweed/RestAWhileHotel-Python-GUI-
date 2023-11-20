import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import csv
from datetime import datetime
from tkcalendar import DateEntry
from tkinter import simpledialog
from DataManager import DataManager




class Manager_Window:
    def __init__(self, main_win):
        
        self.manager_window = tk.Toplevel()
        self.manager_window.title("Rooms Inventory")
        
        # Set a fixed window size (e.g., 650x250)
        self.manager_window.geometry("650x250")
        
        # Make the window non-resizable
        self.manager_window.resizable(False, False)

        # Configure columns if needed
        self.manager_window.columnconfigure(0, minsize=50)
        self.manager_window.columnconfigure(1, minsize=150)
        self.manager_window.columnconfigure(2, minsize=250)
        self.manager_window.columnconfigure(3, minsize=150)

    #**********************************************************************************************************************************************    

        # Creating Labels

          #Creating Label of Main Window
        
        self.title_label = tk.Label(text='Manager View', font=("Helvetica", 15), fg="navy")
        self.title_label.grid(row=0, column=1, columnspan=3)  # Center the label in columns 1, 2, and 3

        dataMgr = DataManager();

        HotelReservationList=dataMgr.GetAllReservationsAsTupleList()
        print (len(HotelReservationList))

        self.FirstFloorKingReservedRoom = 0;
        self.FirstFloorTwinRoom = 0;
        self.FirstFloorDeluxRoom = 0;

        #(userName,floorNumber,roomNumber,cost,startDate)
        for reservation in HotelReservationList:
            if(reservation[1] == "Ground Floor"):
                roomNumber = reservation[2];
                if(roomNumber == "KR1" or roomNumber == "KR2"):
                    self.FirstFloorKingReservedRoom = self.FirstFloorKingReservedRoom + 1;
                elif(roomNumber == "TR1" or roomNumber == "TR2"):
                    self.FirstFloorTwinRoom = self.FirstFloorTwinRoom + 1;
                elif(roomNumber == "DR1" or roomNumber == "DR2"):
                    self.FirstFloorDeluxRoom = self.FirstFloorDeluxRoom + 1;
        
        
        print ("First Floor King Reserver room is " + self.FirstFllorKingReservedRoom);

    def run(self):
        # Start the Tkinter main loop
        self.manager_window.mainloop()

        
