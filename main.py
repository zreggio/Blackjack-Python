from components.data import *
from components.create import *
from objects.game import *

#createGame()


isRunning = True
while(isRunning):
    deck = createDeck()
    game = Game(deck)
    #game.printTest()
    game.update()
    #game.showStartingHand()

    playerInput = input("Run Again?: ")
    if(playerInput == "yes"):
        isRunning = True
    else:
        isRunning = False

