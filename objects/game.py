from components.create import *
class Game:
    def __init__(self, deck):
        self.deck = deck
        self.playerHand = createPlayerHand(deck)
        self.dealerHand = createDealerHand(deck)
        self.outcome = ""

    def printTest(self):
        print("Player Hand:")
        printPlayerHand(self.playerHand)
        print("Dealer Hand:")
        printDealerHand(self.dealerHand)

    def update(self):
        print("----------\nGame Running\n----------")
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
                if(getHandTotal(self.playerHand) > 21):
                    print("Bust")
                    self.outcome = "Player Loss"
                    gameRunning = False
                
                else:
                    gameRunning = True
            elif(playerInput.lower() == "stand"):
                if(getHandTotal(self.playerHand) < getHandTotal(self.dealerHand)):
                    showHand(self)
                    print("Dealer wins!")
                    self.outcome = "Player Loss"
                    gameRunning = False
                elif(getHandTotal(self.playerHand) == getHandTotal(self.dealerHand)):
                    showHand(self)
                    print("Split!")
                    self.outcome = "Split"
                    gameRunning = False
                else:
                    showHand(self)
                    while(getHandTotal(self.playerHand) > getHandTotal(self.dealerHand)):
                        #showHand(self)
                        self.dealerHand.append(self.deck[currCardIndex])
                        showHand(self)
                        currCardIndex += 1
                        if(getHandTotal(self.dealerHand) > 21):
                            print("Player wins!")
                            self.outcome = "Player Win"
                            gameRunning = False
                        elif(getHandTotal(self.dealerHand) > getHandTotal(self.playerHand)):
                            print("Dealer wins!")
                            self.outcome = "Player Loss"
                            gameRunning = False
                        elif(getHandTotal(self.dealerHand) == getHandTotal(self.playerHand)):
                            print("Split!")
                            self.outcome = "Split"
                            gameRunning = False
