import random
from components.data import card_types, suit_types

#card_types = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
#suit_types = ["Spades", "Diamonds", "Clubs", "Hearts"]

def createDeck(cardTypes, suitTypes) -> list:
    card_types = cardTypes
    suit_types = suitTypes
    
    # Generate all possible combinations of card types and suit types
    deck = [f"{card_type} of {suit_type}" for card_type in card_types for suit_type in suit_types]
    
    # Shuffle the deck
    random.shuffle(deck)
    
    return deck

# takes the deck (list) and returns a list of two cards (index: 0, 2)
# for player hand
def createPlayerHand(deck) -> list:
    player_hand = [deck[0], deck[2]]
    return player_hand

# takes the deck (list) and returns a list of two cards (index: 1, 3)
# for dealer hand
def createDealerHand(deck) -> list:
    dealer_hand = [deck[1], deck[3]]
    return dealer_hand

# takes player hand and dealer hand (list type) and returns a list
# of totals coresponding to the card type (queen = 10, 3 = 3, etc...)
# *currently, ace auto evaluates to 1
def calculateStartingTotals(player_hand, dealer_hand) -> list:
    playerSplit_1 = player_hand[0].split(" ")
    playerSplit_2 = player_hand[1].split(" ")

    dealerSplit_1 = dealer_hand[0].split(" ")
    dealerSplit_2 = dealer_hand[1].split(" ")
    
    playerHandSplit = [playerSplit_1, playerSplit_2]
    dealerHandSplit = [dealerSplit_1, dealerSplit_2]

    playerCard_1 = playerHandSplit[0][0]
    playerCard_2 = playerHandSplit[1][0]
    dealerCard_1 = dealerHandSplit[0][0]
    dealerCard_2 = dealerHandSplit[1][0]
    
    playerCardNum_1 = card_types.index(playerCard_1)
    playerCardNum_2 = card_types.index(playerCard_2)
    dealerCardNum_1 = card_types.index(dealerCard_1)
    dealerCardNum_2 = card_types.index(dealerCard_2)

    if(playerCardNum_1 <= 8):
        playerCardNum_1 += 1
    else:
        playerCardNum_1 = 10
    if(playerCardNum_2 <= 8):
        playerCardNum_2 += 1
    else:
        playerCardNum_2 = 10
    if(dealerCardNum_1 <= 8):
        dealerCardNum_1 += 1
    else:
        dealerCardNum_1 = 10
    if(dealerCardNum_2 <= 8):
        dealerCardNum_2 += 1
    else:
        dealerCardNum_2 = 10

    playerTotal = playerCardNum_1 + playerCardNum_2
    dealerTotal = dealerCardNum_1 + dealerCardNum_2

    return [playerTotal, dealerTotal]

def calculateCardTotal(deck, cardIndex) -> int:
    card = deck[cardIndex]
    cardSplit = card.split(" ")

    cardType = cardSplit[0]
    cardNum = card_types.index(cardType)
    if(cardNum <= 8):
        cardNum += 1
    else:
        cardNum = 10
    
    return cardNum

def startGame() -> int:
    gameStarted = True
    dealerDealing = True

    deck = createDeck(card_types, suit_types)
    playerHand = createPlayerHand(deck)
    dealerHand = createDealerHand(deck)
    startingTotals = calculateStartingTotals(playerHand, dealerHand)

    print("\n------------------------------------------------------------")
    print("Player Hand:", playerHand[0], "|||", playerHand[1], "||| Total:", startingTotals[0])
    print("Dealer Hand:", dealerHand[0], "|||", dealerHand[1], "||| Total:", startingTotals[1])
    print("------------------------------------------------------------\n")

    currPlayerTotal = startingTotals[0]
    currDealerTotal = startingTotals[1]
    currCardIndex = 4

    while(gameStarted):
        playerInput = input("\nHit or Stand: ")

        if(playerInput.lower() == "hit"):
            print("Card pulled:", deck[currCardIndex], "\n")
            currPlayerTotal += calculateCardTotal(deck, currCardIndex)
            print("New Player Total:", currPlayerTotal)
            if(currPlayerTotal > 21):
                print("\nBust!")
                gameStarted = False
                toReturn = 2
            currCardIndex += 1

        elif(playerInput.lower() == "stand"):
            while(dealerDealing):
                if(currPlayerTotal > currDealerTotal):
                    currDealerTotal += calculateCardTotal(deck, currCardIndex)
                    print("\nCard:", deck[currCardIndex])
                    print("New Dealer Total:", currDealerTotal)
                elif(currPlayerTotal == currDealerTotal):
                    print("\nEven --- Break")
                    dealerDealing = False
                    gameStarted = False
                    toReturn = 1
                elif(currPlayerTotal < currDealerTotal):
                    print("\nDealer Wins")
                    dealerDealing = False
                    gameStarted = False
                    toReturn = 2
                if(currDealerTotal > 21):
                    print("\nplayer wins")
                    dealerDealing = False
                    gameStarted = False
                    toReturn = 0

                currCardIndex += 1
        elif(playerInput.lower() == "stop"):
            gameStarted = False
            return 3
    return toReturn

def runGame():
    gameRunning = True
    bal = int(input("Please enter # of $ to start with:"))
    while(gameRunning):
        bet = int(input("Bet amount:"))
        outcome = startGame()
        if(outcome == 2):
            bal -= bet
            print("Total $:", bal)
        elif(outcome == 1):
            print("Total $:", bal)
        elif(outcome == 0):
            bal += bet
            print("Total $:", bal)
        print("\n------------------------------------------------------------\n")
        playerInput = input("Play again? (y for yes, n for no)\n")
        if(playerInput == "y"):
            gameRunning = True
        else:
            gameRunning = False

runGame()


