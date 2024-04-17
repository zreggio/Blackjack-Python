from components.create import *
class Game:
    def __init__(self, deck):
        self.playerBal = 100
        self.playerBet = 10
        self.deck = deck
        self.playerHand = createPlayerHand(deck)
        self.dealerHand = createDealerHand(deck)

    def printTest(self):
        print(f'Player Bal: {self.playerBal}')
        print(f'Player Bet: {self.playerBet}')
        print("Player Hand:")
        printPlayerHand(self.playerHand)
        print("Dealer Hand:")
        printDealerHand(self.dealerHand)

    def update(self):
        print("Current Balence:", self.playerBal)
        playerBetInput = input("Enter Bet: ")
        print("----------\nGame Running\n----------")
        self.playerBet = playerBetInput
        showStartingHand(self)

        #playerInput = input("Hit or Stand?\nType 'hit' or 'stand'\n- ")
        currCardIndex = 4
        gameRunning = True
        while(gameRunning):
            playerInput = input("Hit or Stand?\nType 'hit' or 'stand'\n- ")
            if(playerInput.lower() == "hit"):
                self.playerHand.append(self.deck[currCardIndex])
                showStartingHand(self)
                currCardIndex += 1
                gameRunning = True
            elif(playerInput.lower() == "stand"):
                handleDealer(self)
    