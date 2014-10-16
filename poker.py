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

def is_bigger(bigger, smaller):
    rank1 , suit1 = split_card(bigger)
    rank2 , suit2 = split_card(smaller)
    rank1index = ALLOWEDRANKS.index(rank1)
    if rank2 in ALLOWEDRANKS[:rank1index]:
        return True
    return False

