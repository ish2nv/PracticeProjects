import random

money = 100

#Write your game of chance functions here

def coinsim(bet,ht):

    maxval = 13
    num = random.randint(1, maxval)
    val = ""
    iswinner = False
    tempvar = money
    print("##################Coin flip simulator##################")

    if tempvar - bet < 0:
        print("You have insufficient funds to make a " + str(bet) + " bet")
        return 0
    elif bet < 0:
        print("You can't make a bet less than zero")
        return 0        

    else:
        
     if num <=maxval/2:
        val = "Heads"
        if ht == "Heads":
            tempvar = tempvar + bet
            iswinner = True
        elif ht == "Tails":
            tempvar = tempvar - bet
            bet = bet - (bet *2)
            iswinner = False
        else:
            print("Please enter a value of Heads or Tails")
            return 0
            

     else:
        val = "Tails"

        if ht == "Tails":
            tempvar = tempvar + bet
            iswinner = True
        elif ht == "Heads":    
            tempvar = tempvar - bet
            bet = bet - (bet *2)
            iswinner = False
        else:
            print("Please enter a value of Heads or Tails")
            return 0

     if iswinner == True:
        print("The coin is on " + val +". you win!")
        print("You gained " + str(bet))
        print("Your amount is " + str(tempvar))

     else:
        print("The coin is on " + val +". you lose!")        
        print("You lost " + str(bet))
        print("Your amount is " + str(tempvar))
        
     return bet


def chohan(bet,oe):
    
    num = random.randint(1, 10)
    num2 = random.randint(1, 10)
    sum1 = num + num2
    val = ""
    iswinner = False
    tempvar = money

    print("##################Cho-Han##################")

    if tempvar - bet < 0:
        print("You have insufficient funds to make a " + str(bet) + " bet")
        return 0
    elif bet < 0:
        print("You can't make a bet less than zero")
        return 0 

    else:
     if sum1 % 2 == 0:
        val = "Even"

        if oe == "Even":
            tempvar = tempvar + bet
            iswinner = True

        elif oe == "Odd":
            tempvar = tempvar - bet
            bet = bet - (bet *2)
            iswinner = False
        else:
            print("Please enter a value of Even or Odd")
            return 0

     else:
        val = "Odd"
        
        if oe == "Odd":
            tempvar = tempvar + bet
            iswinner = True

        elif oe == "Even":
            tempvar = tempvar - bet
            bet = bet - (bet *2)
            iswinner = False
            
        else:
            print("Please enter a value of Even or Odd")
            return 0

    if iswinner == True:
        print("The result is a " + val +" number. you win!")
        print("You gained " + str(bet))
        print("Your amount is " + str(tempvar))

    else:
        print("The result is a " + val +" number. you lose!")        
        print("You lost " + str(bet))
        print("Your amount is " + str(tempvar))        
    
    return bet


def cardsim(bet):
    player1 = random.randint(1, 10)
    numlist = list(range(1, 11))
    numlist.remove(player1)
    player2 = random.choice(numlist)
    tempvar = money
    
    print("##################Card deck simulator##################")
    
    if tempvar - bet < 0:
        print("You have insufficient funds to make a " + str(bet) + " bet")
        return 0
    elif bet < 0:
        print("You can't make a bet less than zero")
        return 0 
    else:
     if player1 > player2:
        tempvar = tempvar + bet
        print("Player 1 card: " + str(player1))
        print("Player 2 card: " + str(player2))
        print("Player 1 wins!")
        print("")
        print("You gained " + str(bet))
        print("Your amount is " + str(tempvar))     

     elif player2 > player1:
        tempvar = tempvar - bet
        bet = bet - (bet *2)
        print("Player 1 card: " + str(player1))
        print("Player 2 card: " + str(player2))
        print("Player 1 loses!")
        print("")
        print("You lost " + str(bet))
        print("Your amount is " + str(tempvar))        

     else:
        print("Player 1 card: " + str(player1))
        print("Player 2 card: " + str(player2))
        print("Its a tie!")
        print("Your amount is " + str(tempvar))
        return 0

     return bet


def roulette(bet,yourSelection):
    luckynumber = random.randint(1, 36)
    iswinner = False
    tempvar = money
    
    print("##################Roulette##################")
    if tempvar - bet < 0:
        print("You have insufficient funds to make a " + str(bet) + " bet")
        return 0
    elif bet < 0:
        print("You can't make a bet less than zero")
        return 0 
    else:
     if isinstance(yourSelection,int):   
      if yourSelection >= 1 and yourSelection <37:

        if yourSelection == luckynumber:
            tempvar = tempvar + (bet * 35)
            iswinner = True

        else:
            tempvar = tempvar - bet
            bet = bet - (bet *2)
            iswinner = False            
            

     elif yourSelection == "Odd":

        if luckynumber % 2 != 0:
            tempvar = tempvar + bet
            iswinner = True
        else:
            tempvar = tempvar - bet
            bet = bet - (bet *2)  
            iswinner = False            
        

     elif yourSelection == "Even":

        if luckynumber % 2 == 0:
            tempvar = tempvar + bet
            iswinner = True
        else:
            tempvar = tempvar - bet
            bet = bet - (bet *2)
            iswinner = False  

     elif yourSelection == "High":
        if luckynumber > 18 and luckynumber < 37:
            tempvar = tempvar + bet
            iswinner = True
        else:
            tempvar = tempvar - bet
            bet = bet - (bet *2)
            iswinner = False              

     elif yourSelection == "Low":
        if luckynumber > 0 and luckynumber < 19:
            tempvar = tempvar + bet
            iswinner = True
        else:
            tempvar = tempvar - bet
            bet = bet - (bet *2)
            iswinner = False     


     else:
        print("For second parameter, please enter either: ")
        print("A value between 1 - 36\nEven or Odd\nLow (1 - 18) or High (19 - 36)")
        return 0

        
    if iswinner == True:
        print("You selected " + str(yourSelection))
        print("Roulette number is " + str(luckynumber))
        print("")
        print("You won roulette!")
        print("You gained " + str(bet))
        print("Your amount is " + str(tempvar))

        
    else:
        print("You selected " + str(yourSelection))        
        print("Roulette number is " + str(luckynumber))
        print("")
        print("You lost roulette!")
        print("You lost " + str(bet))
        print("Your amount is " + str(tempvar))       

    return bet


#Call your game of chance functions here


money += coinsim(30,"Heads")
money += chohan(22,"Even")
money += cardsim(12)
money += roulette(10,"Even")
