import random
import numpy as np

dealerhand = np.array([random.randint(1,10), random.randint(1,10)])
userhand = np.array([random.randint(1,10), random.randint(1,10)])
gameloop = 1
action = "placeholder"
dealerhit = np.array([random.randint(1,10)])
userhit = np.array([random.randint(1,10)])

def hit():
   global userhand
   global userhit
   userhand = np.concatenate((userhand,userhit))
   print("Your current hand : " + str(userhand) + " (" + str(np.sum(userhand)) + ")")
   userhit = np.array([random.randint(1,10)])

def dealhit():
   global dealerhand
   global dealerhit
   dealerhand = np.concatenate((dealerhand,dealerhit))
   print("Dealer's current hand : " + str(dealerhand) + " (" + str(np.sum(dealerhand)) + ")")
   dealerhit = np.array([random.randint(1,10)])

while gameloop == 1:
    print("D : Let's play a game of blackjack shall we?")
    print("Your current hand : " + str(userhand) + " (" + str(np.sum(userhand)) + ")")
    print("Dealer's current hand : " + str(dealerhand) + " (" + str(np.sum(dealerhand)) + ")")
    action = str(input("What will you do? (h/s) : "))
    while action == "h":
        hit()
        action = str(input("What will you do? (h/s) : "))
    if action == "s":
        print("D : Okay, My turn now.")
        if int(np.sum(userhand)) >= 22:
            print("D : I'm done, you busted.")
        if int(np.sum(dealerhand)) < 10:
            while int(np.sum(dealerhand)) < 10:
                print("D : Hit.")
                dealhit()
        if int(np.sum(dealerhand)) < 17:
            print("D : Hit.")
            dealhit()
        if int(np.sum(dealerhand)) > 17:
            print("D : Stand.")
            print("Dealer's current hand : " + str(dealerhand) + " (" + str(np.sum(dealerhand)) + ")")
    if int(np.sum(userhand)) >= 22:
        print("You lost! You busted.")
    elif int(np.sum(dealerhand)) >= 22:
        print("You won! The dealer busted.")
    elif int(np.sum(userhand)) == int(np.sum(dealerhand)):
        print("it's a stalemate!")
    elif int(np.sum(userhand)) and int(np.sum(dealerhand)) == 21:
        print("It's a stalemate!") 
    elif int(np.sum(userhand)) > int(np.sum(dealerhand)):
        print("You won! Your card was higher than the dealer's!")
    elif int(np.sum(userhand)) < int(np.sum(dealerhand)):
        print("You lost! The dealer's hand was higher than yours!")

    print("Your hand: " + str(userhand) + " (" + str(np.sum(userhand)) + ")")
    print("Dealer's hand : " + str(dealerhand) + " (" + str(np.sum(dealerhand)) + ")")    
    gameloop = int(input("Would you like to play again? (1 = Yes /2 = No) : "))
    dealerhand = np.array([random.randint(1,10), random.randint(1,10)])
    userhand = np.array([random.randint(1,10), random.randint(1,10)])