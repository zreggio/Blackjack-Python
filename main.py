from components.data import *
from components.create import *
from objects.game import *

#createGame()

bal = 100
isRunning = True

while(isRunning):
    print("Player Bal:", bal)
    playerBet = int(input("Enter Bet: "))

    deck = createDeck()
    game = Game(deck)
    game.update()

    if(game.outcome == "Player Win"):
        bal += playerBet
    elif(game.outcome == "Player Loss"):
        bal-= playerBet
    elif(game.outcome == "Split"):
        bal = bal

    playerInput = input("Run Again?: ")
    if(playerInput == "yes"):
        isRunning = True
    else:
        isRunning = False