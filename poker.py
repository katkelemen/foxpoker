# -*- coding: utf8 -*-
SPADES = "S"
HEARTS = "H"
DIAMONDS = "D"
CLUBS = "C"
ALLOWEDRANKS = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
ALLOWEDSUITS = [SPADES, HEARTS, DIAMONDS, CLUBS]
def split_card(card):
    rank = card[:-1]
    suit = card[-1]
    return rank, suit

def is_valid_card(card):
    rank , suit = split_card(card)
    return rank in ALLOWEDRANKS and suit in ALLOWEDSUITS

def is_valid_hand(hand):
    if len(hand) != 5:
        return False
    for card in hand:
        if not is_valid_card(card):
            return False
    sortedhand = sorted(hand)
    for i in range(4):
        if sortedhand[i] == sortedhand[i+1]:
            return False
    return True

def is_bigger_card(bigger, smaller):
    rank1 , suit1 = split_card(bigger)
    rank2 , suit2 = split_card(smaller)
    rank1index = ALLOWEDRANKS.index(rank1)
    if rank2 in ALLOWEDRANKS[:rank1index]:
        return True
    return False

def is_bigger_hand(biggerhand, smallerhand):
    biggerhand_highest = get_highest_card(biggerhand)
    smallerhand_highest = get_highest_card(smallerhand)
    return is_bigger_card(biggerhand_highest, smallerhand_highest)

def get_highest_card(hand):
    highest_card = hand[0]
    for card in hand:
        if is_bigger_card(card, highest_card):
            highest_card = card
    return highest_card

def get_pair(hand):
    ranklist = []
    for card in hand:
        rank, suit = card
        ranklist.append(rank)

def partition(hand):
    return []





