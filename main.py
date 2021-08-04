from art import logo
from replit import clear


print(logo)
bidder = {}
continuous = True
while continuous:
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: $"))
    bidder[name] = bid
    answer = input("Are there any other bidders? Type 'yes' or 'no'. :").lower()
    if answer == "yes":
        continuous = True
        clear()
    elif answer == "no":
        continuous = False
        clear()
score = 0
for bid_value in bidder:
    if bidder[bid_value] >= score:
        score = bidder[bid_value]
    
for bidders in bidder:
    if score == bidder[bidders]:
        print(f"Winner is {bidders} with a bid of ${bidder[bidders]}")
    