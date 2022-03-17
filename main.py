from replit import clear
#HINT: You can call clear() to clear the output in the console.


bid_log = {}

def add_new_dictionary(bidder, bid_amount):

  bid_log[bidder] = bid_amount

continue_bid = True

while continue_bid == True:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: "))
  add_new_dictionary(name, bid)
  clear()
  add_bid = input("Do you want to add a bidder? ").lower()
  
  if add_bid == "no":
    continue_bid = False

max_bid = 0
for name, bid in bid_log.items():
  if bid > max_bid:
    max_bid = bid
    max_bidder = name
    
print(f"{max_bidder} is the highest bidder with ${max_bid}.")