#AUTHOR: ARDA ALP

import random
import time

data = int(input("Which number do you want for find?:")) 
counted = int(input("How many times find it?:")) 

num = random.randrange(0,100)
count = 0

while True:
  if count == counted:
    print("Process Finished...")
    time.sleep(1)
  else:
    print(num)
    time.sleep(0.050) 
    if num == data:
      count += 1
      print("Number Detected",count)
      time.sleep(1)
    num = random.randrange(0,100)
