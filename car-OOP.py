#AUTHOR:ARDA ALP

from datetime import date

todays_date = date.today()

discountRate = 0.2

class car(object):
  
  def __init__(self, brand, model, year, km, price, name="NaN"):
    self.brand = brand
    self.model = model
    self.year = year
    self.km = km
    self.price = price 
    self.age = todays_date.year - self.year 
    self.name = name
   
  def showInfo(self): #Show The Car's Information
    print("Brand:",self.brand)
    print("Model:",self.model)
    print("Year:",self.year,"({} Years Old)".format(self.age))
    print("Kilometers:",self.km)
    print("Price:",self.price)
    if self.name != "NaN":
      print("Name:",self.name)
    
  def discount(self): #Discount The Car Price
    print("Discount Rate:",discountRate)
    disPrice = self.price - (self.price * discountRate)
    print("Discount:",int(self.price * discountRate)) 
    print("New Price:",int(disPrice))
    self.price = disPrice
   
  def cPrice(self): #Change The Car Price
    newPrice = int(input("Enter new price:")) 
    self.price = newPrice
    print("Price Changed As",newPrice) 

  def addKm(self): #Appending The Kilometers 
    append = int(input("How much km do you want append?:"))
    print("{} Kilometers Appended!".format(append))
    self.km = self.km + append
    print("New Km:",self.km)
    
  def cName(self): #Add Or Change The Car Name
    newName = str(input("Enter new name:"))
    if self.name == "NaN":
      print("Name Appended As {}".format(newName))
      self.name = newName
    else:
      print("Name Changed As {}".format(newName))
      self.name = newName
    
x = car("Volkswagen", "GOLF", 2016, 80000, 200000)

