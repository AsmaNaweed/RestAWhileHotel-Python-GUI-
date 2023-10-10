import tkinter as tk
from PIL import Image, ImageTk
from CreateAccountModule import CreateAccountWindow
import csv



class ReserveRoomWindow:    
    def __init__(self):
        print("ReserveRoomWindow Constructor called")
    # get the hotel image      

        self.ReservationWindow = tk.Tk()
        self.ReservationWindow.title("Room Reservation")
        self.ReservationWindow.geometry("800x400")
        self.ReservationWindow.resizable(False, False)       
        img = Image.open(r'C:\Users\\Asma\\Desktop\\Asma.gif')
        img = img.resize((650, 250))
        photo = ImageTk.PhotoImage(img)
        self.labelGIF = tk.Label(image=photo)
        
        self.labelGIF.grid(row= 7, column = 3, columnspan=5, rowspan=20)
          
              
        



    def run(self):
        # Start the Tkinter main loop
        self.ReservationWindow.mainloop()
