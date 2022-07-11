#AUTHOR: ARDA ALP

class user(object):

  def __init__(self, name, surname, age):
    self.name = name
    self.surname = surname
    self.age = age
    
  def info(self):
    print("Name:",self.name)
    print("Surname:", self.surname)
    print("Age:", self.age)

class account(user):

  def __init__(self, name, surname, age, balance=0):
    super().__init__(name, surname, age)
    self.balance = balance
    
  def getBalance(self): 
    print("Your Blance:", self.balance) 
    
  def accountInfo(self):
    self.info()
    print("Balance:",self.balance)
    
  def invest(self):
    amount = int(input("Enter The Amount:")) 
    self.balance += amount
    print("Invest Successful\nNew Balance:", self.balance) 
    
  def withdrawal(self):
    amount = int(input("Enter The Amount:"))
    if amount > self.balance:
      print("Insufficient Balance!")
    else:
      self.balance -= amount
      print("Withdrawal Successful\nNew Balance:", self.balance) 
    
  def getCredit(self):
    self.interestRate = self.age / 1000 #Interest Rate Direct Proportion With Age
    amount = int(input("Enter Credit Amount:"))
    creditReturn = amount + (amount * self.interestRate) 
    self.balance += amount
    print("Credit Process Successful!")
    print("Interest Rate:",self.interestRate) 
    print("New Balance:",self.balance) 
    print("Credit Return:",int(creditReturn))
    
    
x = account("Arda", "Alp", 18)


    