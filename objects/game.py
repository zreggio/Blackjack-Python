from components.create import *


class Game:
    def __init__(self, deck):
        self.deck = deck
        self.playerHand = createPlayerHand(deck)
        self.dealerHand = createDealerHand(deck)
        self.playerTotal = 0
        self.dealerTotal = 0
        self.outcome = ""

    def update(self):
        print("----------\nGame Running\n----------")
        showStartingHand(self)
        currCardIndex = 4
        gameRunning = True
        while gameRunning:
            if getAceCountPlayer(self.playerHand) >= 1:
                self.playerTotal = handlePlayerAce(self.playerHand, self)
            else:
                self.playerTotal = getHandTotal(self.playerHand)
            if self.playerTotal > 21:
                print("\nBust!")
                self.outcome = "Player Loss"
                gameRunning = False
                return
            playerInput = input("Hit or Stand?\nType 'hit' or 'stand'\n- ")
            if playerInput.lower() == "hit":
                self.playerHand.append(self.deck[currCardIndex])
                showStartingHand(self)
                currCardIndex += 1
                if self.playerTotal > 21:
                    print("\nBust")
                    self.outcome = "Player Loss"
                    gameRunning = False
                else:
                    gameRunning = True
            elif playerInput.lower() == "stand":
                if self.playerTotal < getHandTotal(self.dealerHand):
                    showHand(self)
                    print("\nDealer wins!")
                    self.outcome = "Player Loss"
                    gameRunning = False
                elif self.playerTotal == getHandTotal(self.dealerHand):
                    showHand(self)
                    # split = push (named it split incorrectly -- will fix later)
                    print("\nPush")
                    self.outcome = "Split"
                    gameRunning = False
                else:
                    showHand(self)
                    while self.playerTotal > getHandTotal(self.dealerHand):
                        # showHand(self)
                        self.dealerHand.append(self.deck[currCardIndex])
                        showHand(self)
                        currCardIndex += 1
                        if getHandTotal(self.dealerHand) > 21:
                            print("\nPlayer wins!")
                            self.outcome = "Player Win"
                            gameRunning = False
                        elif getHandTotal(self.dealerHand) > self.playerTotal:
                            print("\nDealer wins!")
                            self.outcome = "Player Loss"
                            gameRunning = False
                        elif getHandTotal(self.dealerHand) == self.playerTotal:
                            print("\nPush")
                            self.outcome = "Split"
                            gameRunning = False
