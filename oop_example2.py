#AUTHOR: ARDA ALP

username = str(input("Enter Username: "))
password = str(input("Enter Password: "))

if len(password) <= 3:
  print("Password length must be min 4 characters \nPassword set as: 0000")
  password = "0000"

class user:
  username = username
  password = password
 
  def getName(self):
    print("\n***USERNAME***\nUsername:",self.username)
  
  def getPass(self):
    print("\n***PASSWORD***\nPassword:",self.password)
  
  def info(self):
    print("\n***USER INFORMATION***\nUsername:",self.username,"\nPassword:",self.password)
 
  def cName(self):   
    newName = input("Enter new name: ")
    print("Username changed successfully \nNew Username:",newName)
    self.username = newName
  
  def cPass(self):
    newPass = str(input("Enter new password: ")) 
    if len(newPass) < 4:
      print("Password must be longer than 3 character")
    else:
      print("Password changed successfully \nNew Password:",newPass)
      self.password = newPass
     
user1 = user()
user1.getName()
user1.getPass()
user1.info()

# for see your username -> user1.getName()
# for see your password -> user1.getPass()
# for see your password and username -> user1.info()
# for change your username -> user1.cName()
# for change your password -> user1.cPass("newPassword")
