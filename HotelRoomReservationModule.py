import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import csv
from datetime import datetime


class ReserveRoomWindow:
    def __init__(self, username):
        self.username = username
        self.ReservationWindow = tk.Toplevel()
        self.ReservationWindow.title("Room Reservation")
        self.ReservationWindow.geometry("900x600")
        self.ReservationWindow.resizable(False, False)

        # Load the image (your code)
        try:
            img = Image.open(r'C:\Users\Asma\Desktop\Hotel.jpg')
            img = img.resize((600, 400))
            img = ImageTk.PhotoImage(img)
            self.labelGIF = tk.Label(self.ReservationWindow, image=img)
            self.labelGIF.image = img
            self.labelGIF.place(x=100, y=100)
        except Exception as e:
            print("Error loading image:", str(e))

        # Floor selection
        floorOptionList = ['Ground Floor', 'Second Floor', 'Third Floor']
        self.floorOption_var = tk.StringVar()
        self.floorOption_var.set('Select Floor')
        self.floorOption_menu = tk.OptionMenu(self.ReservationWindow, self.floorOption_var, *floorOptionList)
        self.floorOption_menu.grid(row=1, column=1)
        self.floorOption_var.trace('w', self.handle_floor_selection)

        # Create a drop-down menu for room type selection
        room_types = [
            "KR – King Room 4 per floor $59.00",
            "TR – Twin Room 2 per floor $69.00",
            "DR – Deluxe King Room 4 per floor $75.00",
            "CR – Corner King Room 4 per floor $90.00",
            "CS – Corner Suite 2 per floor $110.00"
        ]

        self.selected_room_type = tk.StringVar()
        self.selected_room_type.set("Select Room")

        self.room_menu = tk.OptionMenu(self.ReservationWindow, self.selected_room_type, *room_types,
                                       command=self.room_selection)
        self.room_menu.place(x=20, y=50)
        self.room_menu.config(width=22, state="disabled")  # Disabled by default

        # Create buttons for reservation and cancellation
        self.reserve_button = tk.Button(self.ReservationWindow, text="Reserve Room", command=self.reserve_room)
        self.reserve_button.place(x=20, y=80)

        self.cancel_button = tk.Button(self.ReservationWindow, text="Cancel Reservation", command=self.cancel_reservation)
        self.cancel_button.place(x=150, y=80)

    def room_selection(self, selected_room_type):
        print("Selected Room Type:", selected_room_type)

    def reserve_room(self):
        selected_floor = self.floorOption_var.get()
        selected_room_info = self.selected_room_type.get()

        if selected_floor != 'Select Floor' and selected_room_info != 'Select Room':
            room_type, price_info = selected_room_info.split(" – ")
            price, _ = price_info.split(" $")
            print("Selected Room Type:", room_type)
            print("Price:", price)
            ReservationCost="100"
            ReservationStartDate="1-1-2023"
            ReservationEndDate="2-2-2023"

            # Save the reservation details to a file (user-specific)
            reservation_data = f"{self.username},{selected_floor},{room_type},{ReservationCost},{ReservationStartDate},{ReservationEndDate}\n"
            #python2023,First Floor,123,King KR,2023-10-11,2034-10-20
            with open('reservationData.txt', mode='a') as file:
                file.write(reservation_data)

            # Show a message box
            messagebox.showinfo("Room Reservation", "Your room has been reserved.")

            # Clear the selected options
            self.floorOption_var.set('Select Floor')
            self.selected_room_type.set('Select Room')
        else:
            messagebox.showerror("Error", "Please select both floor and room type.")

    def cancel_reservation(self):
        # You can implement the cancellation logic here
        pass

    def handle_floor_selection(self, *args):
        selected_floor = self.floorOption_var.get()
        if selected_floor:
            print("Selected Floor:", selected_floor)
            self.room_menu.config(state="normal")  # Enable room selection

            
    def ReadAllReservation (self,fileNameToRead:str):
        with open(fileNameToRead, "r") as f:
            lines = f.readlines()
            return lines;
    def FindRservationRecord(self,usernameToSearch,room_number,AllLinesData):
        for line in AllLinesData:
            print(line)
def main():
    username =  "Asma" # Replace with the actual username after login
    ReserveWindow=ReserveRoomWindow(username)
    StoreLines=ReserveWindow.ReadAllReservation(r"C:\Development\Python\RestAWhileHotel\reservationData.txt")
    ReserveWindow.FindRservationRecord("Python2023",15,StoreLines)

   
    
    

if __name__ == "__main__":
    main()




   
