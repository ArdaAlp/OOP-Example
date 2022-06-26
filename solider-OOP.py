#AUTHOR: ARDA ALP

class solider:
  hp = 100
  ammo = 24
  damage = 8
  
  def stats(self):
    print("HP:",self.hp, "\nAMMO:",self.ammo, "\nDAMAGE:",self.damage)
  
  def attack(self):
    if self.ammo <=0:
      print("No ammo, you can't attack!")
    elif self.hp <=0:
      print("You wasted please firstly respawn")
    else:
      self.hp -= 10
      self.ammo -= 12
      print("You attacked!\nGived",((24 - self.ammo) * self.damage),"damage")
     
  def kill(self):
    self.hp = 0
    print("Wasted")
   
  def spawn(self):
    self.hp = 100
    print("You respawned")
  
  def boost(self):
    print("You boosted new stats:")
    self.hp += 50
    self.ammo += 12
    self.damage += 2
    print(self.stats())
   
solider1 = solider()

# for see stats -> solider1.stats()
# for attack -> solider1.attack()
# for kill yourself -> solider1.kill()
# for respawn -> solider1.spawn()
# for boost -> solider1.boost()
