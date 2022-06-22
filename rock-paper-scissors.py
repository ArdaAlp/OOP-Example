#AUTHOR:ARDA ALP

import random as rdm

moves = ("rock", "paper", "scissors")

data = int(input("Enter Your Move Number \n1-Rock \n2-Paper \n3-Scissors \nYour Move:"))

if data >= 4:
  print("Move number doesn't found")

else:

  userMove = data - 1
  user = moves[userMove] 

  compMove = rdm.randrange(0,3)
  comp = moves[compMove]
  
  if comp == "rock" and user == "scissors" or comp == "paper" and user == "rock" or comp == "scissors" and user == "paper":
    print("----------\nComputer:", comp, "\nYou:", user, "\n----------\nCOMPUTER WON!")

  elif comp == user:
    print("----------\nDraw!")
 
  else:
    print("----------\nComputer:", comp, "\nYou:", user, "\n----------\nYOU WON!") 
