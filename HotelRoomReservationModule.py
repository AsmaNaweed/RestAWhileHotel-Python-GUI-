import tkinter as tk
from PIL import Image, ImageTk

class ReserveRoomWindow:
    def __init__(self):
        print("ReserveRoomWindow Constructor Called.");
        self.ReservationWindow = tk.Tk();
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

        # Floor selection (your code)
        floorOptionList = ['Ground Floor', 'Second Floor', 'Third Floor']
        self.floorOption_var = tk.StringVar()
        self.floorOption_var.set('Select Floor')
        self.floorOption_menu = tk.OptionMenu(self.ReservationWindow, self.floorOption_var, *floorOptionList)
        self.floorOption_menu.grid(row=1, column=1)
        self.floorOption_var.trace('w', self.get_floor_info)

        # Create a drop-down menu for room type selection (your code)
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

        # Create a reserve button (your code)
        self.reserve_button = tk.Button(self.ReservationWindow, text="Reserve Room", command=self.reserve_room)
        self.reserve_button.place(x=20, y=80)
        

    def room_selection(self, selected_room_type):
        print("Selected Room Type:", selected_room_type)

    def reserve_room(self):
        selected_room_info = self.selected_room_type.get()
        if selected_room_info:
            # Extract room type and price from the selected option (your code)
            room_type, price_info = selected_room_info.split(" – ")
            price, _ = price_info.split(" $")
            print("Selected Room Type:", room_type)
            print("Price:", price)

            # Save the reservation details to a file (your code)
            with open('reservationData.txt', mode='a') as file:
                file.write(f"Room Type: {room_type}, Price: {price}\n")

    def get_floor_info(self, *args):
        selected_floor = self.floorOption_var.get()
        if selected_floor:
            print("Selected Floor:", selected_floor)

rw = ReserveRoomWindow()
tk.mainloop();