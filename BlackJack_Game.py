############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import art_blackjack
import os
def Deal_Cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card

def Calculate_Score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def Conditions(user_score,computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def Play_Game():
    User_Card=[]
    Computer_Card=[]
    end=True
    for _ in range(2):
        User_Card.append(Deal_Cards())
        Computer_Card.append(Deal_Cards())

    print(art_blackjack.logo)
    while end:
        user_score=Calculate_Score(User_Card)
        comp_score=Calculate_Score(Computer_Card)

        print(f"Your cards: {User_Card}, current score: {user_score}")
        print(f"Computer's first card: {Computer_Card[0]}")

        if user_score == 0 or comp_score == 0 or user_score>21:
            end=False
        else:
            user_next_deal=input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_next_deal == 'y' or user_next_deal == 'yes':
                User_Card.append(Deal_Cards())
            else:
                end=False
    while comp_score!= 0 and comp_score <=17:
        Computer_Card.append(Deal_Cards())
        comp_score=Calculate_Score(Computer_Card)
        print(f"Your cards: {User_Card}, current score: {user_score}")
        print(f"Computer's final hand: {Computer_Card}, final score: {comp_score}")
        print(Conditions(user_score,comp_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    os.system('cls')
    Play_Game()