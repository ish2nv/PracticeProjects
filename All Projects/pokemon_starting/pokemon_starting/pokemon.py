class Pokemon:
  def __init__(self, name = "Charmander", level = 1,p_type = "Fire",maxhealth = 3,currenthealth = 3,ko = False,xp = 1):
    self.name = name
    self.level = level
    self.p_type = p_type
    self.maxhealth = maxhealth
    self.currenthealth = currenthealth
    self.ko = ko
    self.xp = xp

    if self.level <= 0:
        self.level = 1

    if self.maxhealth <= 0:
        self.maxhealth = 3
        
    if self.currenthealth <= 0:
        self.currenthealth = 3
        
    if self.xp <= 0:
        self.xp = 1

    if self.p_type != "Fire" and self.p_type !="Water" and self.p_type != "Grass":
        self.p_type = "Fire"
        print("wrong type inputted for " + self.name + ". type automatically set to Fire")

        

  def lose_health(self,damage):
      self.currenthealth = self.currenthealth - damage

      if self.currenthealth <= 0:
          self.currenthealth = 0
          self.knockout()

      print("Your " +str(self.name)+ " now has "+str(self.currenthealth)+" health")

  def lose_health(self,opponent,damage):
      opponent.currenthealth = opponent.currenthealth - damage

      if opponent.currenthealth <= 0:
          opponent.currenthealth = 0
          opponent.knockout()

      print("Your opponents " + str(opponent.name)+ " now has "+str(opponent.currenthealth)+" health")

  def getko(self):
      return self.ko
    
  def getname(self):
      return self.name

  def getcurrenthealth(self):
      return self.currenthealth
    
  def knockout(self):
      self.ko = True
      print(str(self.name) + " has been knocked out.")


  def revive(self):
      self.ko = False
      print(str(self.name) + " has been revived by potion.")


  def gain_health(self,boost):
      self.currenthealth = self.currenthealth + boost
      if self.currenthealth >= self.maxhealth:
          self.currenthealth = self.maxhealth
      print(str(self.name)+ " now has "+str(self.currenthealth)+" health")


  def attack(self,opponent):

      if self.p_type == "Water" and opponent.p_type == "Fire":
          print("Your attack was effective! " + str(self.level*float(2)) + " damage" )
          self.lose_health(opponent,self.level*float(2))
          self.increaseXP(self.level*float(2))
          
      elif self.p_type == "Fire" and opponent.p_type == "Water":
          print("Your attack was ineffective! "+ str(self.level/float(2)) + " damage" )
          self.lose_health(opponent,self.level/float(2))
          self.increaseXP(self.level/float(2))
          
      elif self.p_type == "Fire" and opponent.p_type == "Grass":
          print("Your attack was effective! "+ str(self.level*float(2)) + " damage" )
          self.lose_health(opponent,self.level*float(2))
          self.increaseXP(self.level*float(2))
          
      elif self.p_type == "Grass" and opponent.p_type == "Fire":
          print("Your attack was ineffective! "+ str(self.level/float(2)) + " damage" )
          self.lose_health(opponent,self.level/float(2))
          self.increaseXP(self.level/float(2))

      elif self.p_type == "Grass" and opponent.p_type == "Water":
          print("Your attack was effective! "+ str(self.level*float(2)) + " damage" )
          self.lose_health(opponent,self.level*float(2))
          self.increaseXP(self.level*float(2))
          
      elif self.p_type == "Water" and opponent.p_type == "Grass":
          print("Your attack was ineffective! " + str(self.level/float(2)) + " damage" )
          self.lose_health(opponent,self.level/float(2))
          self.increaseXP(self.level/float(2))
          
      else:
          print(str(float(self.level)) + " damage" )          
          self.lose_health(opponent,float(self.level))
          self.increaseXP(float(self.level))
          
  def level_up(self):
      self.level = self.level + 1
      self.maxhealth = self.level * 5
      self.evolvePokemon()
      print("Your " + str(self.name) + " is now at level " + str(self.level))
      

  def evolvePokemon(self):
      if self.level >=5 and self.level < 10:
          self.name = self.name +" 2.0"
          self.maxhealth = self.level * 10
          print("")
          print("Your pokemon is glowing....")
          print("Congratulations! Your pokemon evolved into a " + str(self.name))
          
      elif self.level >=10:
          self.name = self.name +" 3.0"
          self.maxhealth = self.level * 10
          print()
          print("Your pokemon is glowing....")
          print("Congratulations! Your pokemon evolved into a " + str(self.name))
          
  def increaseXP(self,amount):
      self.xp = self.xp + amount
      print("Your " + str(self.name) + " gained "+ str(self.xp) + " xp")
      
      if self.xp >= self.level * 5:
          self.level_up()
      

      


class Trainer:

  def __init__(self, pokemonstorage, name,potions,active):
    self.pokemonstorage = pokemonstorage
    self.name = name
    self.potions = potions
    self.active = active

    counter = 0

    if self.potions <=0:
        self.potions = 1
    
    if len(self.pokemonstorage) > 6:
        for i in range(6,len(self.pokemonstorage)):
            del self.pokemonstorage[i]
            counter = counter + 1

        print(str(counter) + " extra pokemons removed from the storage of " + str(self.name))

    
  def attack_other_trainer(self, othertrainer):
      print("################"+str(self.name)+" attacks################")
      print(str(self.pokemonstorage[self.active].getname()) + " vs " +str(othertrainer.pokemonstorage[othertrainer.active].getname()) )

      if self.pokemonstorage[self.active].getcurrenthealth() <= 0:
          print("Your current pokemon is knocked out. Choose another, or use potion")
          
          
      elif othertrainer.pokemonstorage[othertrainer.active].getcurrenthealth() <= 0:
          print("Your opponents pokemon is knocked out. Let them choose another pokemon before attacking")



      else:
          self.pokemonstorage[self.active].attack(othertrainer.pokemonstorage[othertrainer.active])
      
    
  def usePotion(self,newpotion):
      print("################"+str(self.name)+" uses a potion################")
      if newpotion <= 0:
        print("Please use a potion greater than 0 effect")
      else:
        print("You used a potion on your " + self.pokemonstorage[self.active].getname())

        self.potions = newpotion  
        self.pokemonstorage[self.active].gain_health(self.potions)

        if self.pokemonstorage[self.active].getko() == True:
           self.pokemonstorage[self.active].revive()
          
      

  def switchActive(self,chooseActive):
      print("################"+str(self.name)+" switches pokemon################")
      if len(self.pokemonstorage)>0:
          if chooseActive >=0 and chooseActive < len(self.pokemonstorage):
           oldactive = self.active   
           self.active = chooseActive            
           if self.pokemonstorage[self.active].getko() == True:
              print("Current active pokemon, " + str(self.pokemonstorage[self.active].getname()) + " is knocked out. Use potion to revive or swap with a healthy pokemon")
           else:
              print("Swapped " + str(self.pokemonstorage[oldactive].getname()) + " with " + str(self.pokemonstorage[chooseActive].getname() + " as the active pokemon") )
          else:
              print("Choose a pokemon you want active within the bounds of your pokemon storage")
      else:
          print("Choose a pokemon you want active within the bounds of your pokemon storage")
      

PokemonA = Pokemon()
PokemonB = Pokemon("Bulbasaur",1,"Grass",3,3,False,1)
PokemonC = Pokemon("Squirtle",1,"Water",3,3,False,1)
PokemonD = Pokemon("Chimchar",1,"Fire",3,3,False,1)
PokemonE = Pokemon("Totodile",1,"Water",3,3,False,1)
PokemonF = Pokemon("Chicorita",1,"Grass",3,3,False,1)
PokemonG = Pokemon("Cyndaquil",1,"Fire",3,3,False,1)
PokemonH = Pokemon("Treecko",1,"Grass",3,3,False,1)
PokemonI = Pokemon("Vaporeon",1,"Water",3,3,False,1)
PokemonJ = Pokemon("Tangela",1,"Grass",3,3,False,1)
PokemonK = Pokemon("Ponyta",1,"Fire",3,3,False,1)
PokemonL = Pokemon("Psyduck",1,"Water",3,3,False,1)



trainerA = Trainer([PokemonA,PokemonB,PokemonC,PokemonD,PokemonE,PokemonF],"Shah",30,0)
trainerB = Trainer([PokemonG,PokemonH,PokemonI,PokemonJ,PokemonK,PokemonL],"Ash Ketchum",30,0)

trainerA.attack_other_trainer(trainerB)
trainerB.attack_other_trainer(trainerA)
trainerA.attack_other_trainer(trainerB)
trainerB.attack_other_trainer(trainerA)
trainerA.attack_other_trainer(trainerB)
trainerB.switchActive(2)
trainerA.usePotion(3)
trainerB.attack_other_trainer(trainerA)
trainerA.attack_other_trainer(trainerB)
trainerB.attack_other_trainer(trainerA)
trainerA.switchActive(1)
trainerB.attack_other_trainer(trainerA)


