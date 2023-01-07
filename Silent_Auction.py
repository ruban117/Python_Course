import art2
import os

print(art2.logo)

print("Welcome to the secret auction program.")

bidders={}

def Bidders_Details(n_bidders):
    highest_bid=0
    winner=""
    for b in n_bidders:
        bid_amount=n_bidders[b]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=b
    print(f"The winner is {winner} with a bid of ${highest_bid}")
end=True
while end:
    name=input("What is your name?:\n")
    bid=int(input("What is your bid?: $"))
    bidders[name]=bid
    popup=input("Are there any other bidders?: type 'yes' or 'no' :").lower()
    if popup == 'yes':
        os.system('cls')
    else:
        os.system('cls')
        end=False
        Bidders_Details(bidders)
