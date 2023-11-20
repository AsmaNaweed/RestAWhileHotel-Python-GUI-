import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import csv
from datetime import datetime
from tkcalendar import DateEntry
from tkinter import simpledialog
from ManagerDataModule import Manager_Window


class ReserveRoomWindow:  
 
            
    def __init__(self, main_window, username):
        self.username = username
        self.main_window = main_window
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



        #Calendar

        #Start-Date Label
        startDateLabel = tk.Label(self.ReservationWindow, text='Choose Start date');
        startDateLabel.place(x=350,y=20)

        self.StartDateControl = DateEntry(self.ReservationWindow, width=12, background='darkblue',
                    foreground='white', borderwidth=2)
        self.StartDateControl.place(x=450,y=20);

        #End_Date Label
        EndDateLabel = tk.Label(self.ReservationWindow, text='Choose End date');
        EndDateLabel.place(x=350,y=80)

        self.EndDateControl = DateEntry(self.ReservationWindow, width=12, background='darkblue',
                    foreground='white', borderwidth=2)
        self.EndDateControl.place(x=450,y=80);
 

        # Create a drop-down menu for room type selection
        room_types = [
            "KR1 - King Room - $59.00",
            "KR2 - King Room - $59.00",
            "KR3 - King Room - $59.00",
            "KR4 - King Room - $59.00",
            "TR1 - Twin Room - $69.00",
            "TR2 - Twin Room - $69.00",
            "DR1 - Deluxe King - $75.00",
            "DR2 - Deluxe King - $75.00",
            "DR3 - Deluxe King - $75.00",
            "DR4 - Deluxe King - $75.00",
            "CR1 - Corner King - $90.00",
            "CR2 - Corner King - $90.00",
            "CR2 - Corner King - $90.00",
            "CR3 - Corner King Room - $90.00",
            "CR4 - Corner King Room - $90.00",
            "CS1 - Corner Suite - $110.00",
            "CS2 - Corner Suite - $110.00"
            
          ]
        self.user_reservations = self.GetReservationsByUser(self.username)
        self.selected_room_type = tk.StringVar()
        self.selected_room_type.set("Select Room")
        self.selected_reservation_for_cancellation=tk.StringVar()

        self.room_menu = tk.OptionMenu(self.ReservationWindow, self.selected_room_type, *room_types,
                                       command=self.room_selection)
        self.room_menu.place(x=20, y=50)
        self.room_menu.config(width=22, state="disabled")  # Disabled by default

        # Create buttons for reservation and cancellation
        self.reserve_button = tk.Button(self.ReservationWindow, text="Reserve Room", command=self.reserve_room)
        self.reserve_button.place(x=20, y=80)

         # Creating Manager Button
        self.Manager_button = tk.Button(self.ReservationWindow, text="Manager", command=self.ManagerButtonClicked)
        self.Manager_button.place(x=650, y=40)  # Position the "Manager" button in column 10

               
          # Create a label for the cancellation menu
        cancel_label = tk.Label(self.ReservationWindow, text="Cancel Reservation:")
        cancel_label.place(x=200, y=50)
       
        self.cancel_reservation_menu = tk.OptionMenu(self.ReservationWindow, self.selected_reservation_for_cancellation, *self.user_reservations,
                                       command=self.cancel_reservation)
        self.cancel_reservation_menu.place(x=150, y=80)
        self.cancel_reservation_menu.config(width=25)
        
    def ManagerButtonClicked(self):
      print("Manager button clicked")
         # Disable the Reservation window
      self.ReservationWindow.withdraw()

      print("Manager button clicked")
        
        
    # Create an instance of the Manager_Window class
      self.manager_window_instance = Manager_Window(self.main_window)

        
        # Run the login manager and display the login 
      print("calling run")
      self.manager_window_instance.run()

       

    def room_selection(self, selected_room_type):
        room_info = selected_room_type.split("-")
        room_number = room_info[0].strip()

        # Check room availability
        if self.is_room_available(self.floorOption_var.get(), room_number):

            print ("Selected Room Type: " , selected_room_type)
        else:
            messagebox.showerror("Room Unavailable" , " This room is already reserved. Please select another room.")



    def is_room_available(self, selected_floor, room_number):
       # cleaned_room_number =  room_number.replace(" ", "").upper()  # Remove spaces and convert to uppercase

        # Implement logic to check if the room is available based on its status
        #return self.room_types_data[cleaned_room_number]["status"] == "available"
        #print("Selected Room Type:", selected_room_type)
        allReservations=self.ReadAllReservations("reservationData.txt")
        if self.DoesReservationExists(selected_floor,room_number,allReservations):
            return False
        else:
            return True
        

    def ReadAllReservations(self,fileNameToRead:str):
        with open(fileNameToRead, "r") as f:
            lines = f.readlines()
            return lines;
        
    def DoesReservationExists(self,usernameToSearch,selected_floor,room_number,AllLinesData):
        for line in AllLinesData:
            #userName,FloorNumber,RoonNumber,Cost,StartDate,EndDate
             userName,floorNumber,roomNumber,_,_,_ = line.split(",")
             if (userName == usernameToSearch and floorNumber == selected_floor and roomNumber == room_number):
                 return True
        return False

    def DoesReservationExists(self,selected_floor,room_number,AllLinesData):
        for line in AllLinesData:
            #userName,FloorNumber,RoonNumber,Cost,StartDate,EndDate
            _,floorNumber,roomNumber,_,_,_ = line.split(",")
            if ( floorNumber == selected_floor and roomNumber == room_number):
                 return True
        return False

    def ValidateReservation(self, userName, selectedFloor, roomNumber, startDate, endDate):
        # Check room availability before reserving the room
            if not self.is_room_available(selectedFloor,roomNumber):
                messagebox.showerror("Room Uavailable" , " This room is already reserved. Please select another room.")
                return False
            else:
                return True
        
    

    def reserve_room(self):
        selected_floor = self.floorOption_var.get()
        selected_room_info = self.selected_room_type.get()
        print(selected_room_info)       

        if selected_floor != 'Select Floor' and selected_room_info != 'Select Room':
            room_number,_,reservation_cost = selected_room_info.split("-")
            room_number = room_number.strip()  # Strip whitespace from room_number          
        
                  
            reservation_start_date=self.StartDateControl.get_date()

            reservation_end_date=self.EndDateControl.get_date()


            isReservationValid= self.ValidateReservation(self.username,selected_floor,room_number,reservation_start_date,reservation_end_date)
            if isReservationValid == False:
                return     
           
            

            # Save the reservation details to a file (user-specific)
            reservation_data = f"{self.username},{selected_floor},{room_number},{reservation_cost},{reservation_start_date},{reservation_end_date}\n"
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

    def cancel_reservation(self, selected_reservation):
        print (selected_reservation)
        userReservations=self.GetReservationsByUser(self.username)
        if len(userReservations)==0:
            messagebox.showerror("ERROR","No Reservations found")
            return
        
              
            # Extract details
        userNameToDelete, floorNumberToDelete, roomNumberToDelete, cost, startDateToDelete = selected_reservation
            #Call the DeleteReservation function to cancel the reservation
        self.DeleteReservation(userNameToDelete, floorNumberToDelete, roomNumberToDelete, cost, startDateToDelete)

            # Show a success message
        messagebox.showinfo ("Successful", "Reservation Deleted.")
 
       
    def DeleteReservation(self,userNameToDelete,floorNumberToDelete,roomNumberToDelete,cost,startDateToDelete):
        #print(f"I will delete {userName},{floorNumber},{roomNumber},{cost},{startDate}")
        allLines=self.ReadAllReservations("reservationData.txt")
        with open('reservationData.txt', mode='w') as file:
             for line in allLines:
                 userName,floorNumber,roomNumber,_,startDate,_ = line.split(",")
                 if not(userName == userNameToDelete and floorNumberToDelete == floorNumber and roomNumberToDelete == roomNumber and startDateToDelete.strip() == startDate.strip()):
                    file.write(line)
        
        

        
    def GetReservationsByUser(self,searchUserName):
        reservationList = []
        allLines=self.ReadAllReservations("reservationData.txt")
        for line in allLines:
          userName,floorNumber,roomNumber,cost,startDate,_ = line.split(",")
          if (searchUserName==userName):
              reservationList.append((userName,floorNumber,roomNumber,cost,startDate))
        return reservationList;
              
          
            

    def handle_floor_selection(self, *args):
        selected_floor = self.floorOption_var.get()
        if selected_floor:
            print("Selected Floor:", selected_floor)
            self.room_menu.config(state="normal")  # Enable room selection



                
    
             
"""def main():
    username =  "Asma" # Replace with the actual username after login
    ReserveWindow=ReserveRoomWindow(_,username)
    myReservations=ReserveWindow.GetReservationsByUser("Asma")
    print (len(myReservations))
    for reservation in myReservations:
        userName,floorNumber,roomNumber,cost,startDate=reservation
        
        print(userName)
   
        
    

main()"""
    
    



