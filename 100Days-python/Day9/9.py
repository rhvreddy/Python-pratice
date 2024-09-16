## The Secret Auction Program Instructions and Flow Chart


# Step1: Ask the user for input

# name = input("What is your name?: ")
# price = int(input("What is your bid? $"))

# bids = {}
# Step2: Save data into dictionary {name: price}

# bids[name] = price
# Step3: whether if new bids need to be added
# should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")

# bids = {}
# continue_bidding = True
# while continue_bidding:
#     name = input("What is your name?: ")
#     price = int(input("What is your bid? $"))
#     bids[name] = price
#     should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
#     if should_continue == "no":
#         continue_bidding = False
#         find_highest_bidder(bids)
#     elif should_continue == "Yes":
#         print("\n" * 20)


# Step4: Compare bids in dictionary

# def find_highest_bidder(bidding_dictionary):
#     highest_bid = 0
#     for bidder in  bidding_dictionary:
#         bid_amount = bidding_dictionary[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder
#     print(f"The winner is {winner} with a bid of ${highest_bid}.")



# max(fruits, key=fruits.get) ==>This command help us print the hight number from the list



def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    for bidder in  bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "Yes":
        print("\n" * 20)