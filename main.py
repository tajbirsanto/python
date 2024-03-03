from art import logo
from replit import clear

print(logo)

bidders={}

bidding_finished=False

def find_highest_bidder(bidding_record):
  highest_bidder=0
  winner=""
  for bidder in bidding_record:
    bid_amount= bidding_record[bidder]
    if bid_amount>highest_bidder:
      highest_bidder=bid_amount
      winner=bidder
      print(f"The winner is {winner} with a bid of ${highest_bidder}")
    


while not bidding_finished:
  name=input(f"What is your name? ")
  bid=int(input(f"What is your bid? $"))
  bidders[name]=bid
  should_finished=input(f"Are there any other bidders? Type  'yes' or 'no'  : \n")
  if should_finished=="no":
     bidding_finished=True
     find_highest_bidder(bidders)
  elif should_finished=="yes":
    clear()