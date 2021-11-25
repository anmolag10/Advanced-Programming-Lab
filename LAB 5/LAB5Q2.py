class Vehicle:
    def __init__(self,name,ID,manu):
        self.name = name
        self.id = ID
        self.manuName=name

class Passenger(Vehicle):
    def __init__(self, name, ID, manu,num):
        super().__init__(name, ID, manu)
        self.noPassenger=num
    
    def display(self):

        print( "Details:" + self.name+ " " + self.id+ " "+ self.manuName + " "+ self.noPassenger)


if __name__ =="__main__":
    p1 = Passenger("TataSumo","DL3C1231","Tata Moter","88")

    p1.display()