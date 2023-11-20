class DataManager:

    



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

        
   def DeleteReservation(self,userNameToDelete,floorNumberToDelete,roomNumberToDelete,cost,startDateToDelete):
        #print(f"I will delete {userName},{floorNumber},{roomNumber},{cost},{startDate}")
        allLines=self.ReadAllReservations("reservationData.txt")
        with open('reservationData.txt', mode='w') as file:
             for line in allLines:
                 userName,floorNumber,roomNumber,_,startDate,_ = line.split(",")
                 if not(userName == userNameToDelete and floorNumberToDelete == floorNumber and roomNumberToDelete == roomNumber and startDateToDelete.strip() == startDate.strip()):
                    file.write(line)
        
        

        
   def GetAllReservationsAsTupleList(self):
        reservationList = []
        allLines=self.ReadAllReservations("reservationData.txt")
        for line in allLines:
          userName,floorNumber,roomNumber,cost,startDate,_ = line.split(",")          
          reservationList.append((userName,floorNumber,roomNumber,cost,startDate))
        return reservationList;

        
              
          
