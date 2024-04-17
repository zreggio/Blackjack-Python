import random
from objects.card import Card
from components.data import card_types, suit_types

def handleDealer(game):
    if(getHandTotal(game.dealerHand) == 21):
        return "stand"
    elif(getHandTotal(game.dealerHand) > 21):
        return "bust"
    elif(getHandTotal(game.playerHand) > getHandTotal(game.dealerHand)):
        return "hit"
    elif(getHandTotal(game.playerHand) == getHandTotal(game.dealerHand)):
        return "stand"
    elif(getHandTotal(game.playerHand) < getHandTotal(game.dealerHand)):
        return "stand"

def showStartingHand(game):
        print("\n----------")
        print(f'Player Bal: {game.playerBal}')
        print(f'Player Bet: {game.playerBet}')
        print("----------")
        print("Player Hand:", getHandTotal(game.playerHand))
        printPlayerHand(game.playerHand)
        print("----------")
        print("Dealer Hand:", getHandTotalStart(game.dealerHand))
        printStartingDealerHand(game.dealerHand)
        print("----------")

def showHand(game):
    print("\n----------")
    print(f'Player Bal: {game.playerBal}')
    print(f'Player Bet: {game.playerBet}')
    print("----------")
    print("Player Hand:", getHandTotal(game.playerHand))
    printPlayerHand(game.playerHand)
    print("----------")
    print("Dealer Hand:", getHandTotal(game.dealerHand))
    printStartingDealerHand(game.dealerHand)
    print("----------")

def createDeck() -> list:
    deck = [Card(f"{card_type} of {suit_type}", 0) for card_type in card_types for suit_type in suit_types]
    random.shuffle(deck)
    createValues(deck)
    return deck

def createPlayerHand(deck) -> list:
    player_hand = [deck[0], deck[2]]
    return player_hand

def createDealerHand(deck) -> list:
    dealer_hand = [deck[1], deck[3]]
    return dealer_hand

def createValues(deck) -> list:
    for card in deck:
        if(card.name.split(" ")[0] == "Ace"):
            card.value = 1
        elif(card.name.split(" ")[0] == "Two"):
            card.value = 2
        elif(card.name.split(" ")[0] == "Three"):
            card.value = 3
        elif(card.name.split(" ")[0] == "Four"):
            card.value = 4
        elif(card.name.split(" ")[0] == "Five"):
            card.value = 5
        elif(card.name.split(" ")[0] == "Six"):
            card.value = 6
        elif(card.name.split(" ")[0] == "Seven"):
            card.value = 7
        elif(card.name.split(" ")[0] == "Eight"):
            card.value = 8
        elif(card.name.split(" ")[0] == "Nine"):
            card.value = 9
        else:
            card.value = 10

def printDeck(deck):
    for card in deck:
        print(card.name, "---", card.value)

def printPlayerHand(player_hand):
    for card in player_hand:
        print("-", card.name)

def printDealerHand(dealer_hand):
    for card in dealer_hand:
        print("-", card.name)

def printStartingDealerHand(dealer_hand):
    print("-", dealer_hand[0].name)

def getHandTotal(hand) -> int:
    currTotal = 0
    for card in hand:
        currTotal += card.value
    return currTotal

def getHandTotalStart(hand) -> int:
    currTotal = hand[0].value
    return currTotal
