print("Welcome to secret auction program")
my_dict = {}


def bidders(bidder_name, bidder_amount):
    my_dict[bidder_name] = bidder_amount


def ask_for_response():
    name = input('what is your name? ')
    bid = int(input('what is your bid?: ₹'))
    bidders(bidder_name=name, bidder_amount=bid)
    response = input('are there any other bidder? type yes or no\n').lower()
    if response == "yes":
        ask_for_response()


ask_for_response()
winner = ''
amount = 0
for key in my_dict:
    if my_dict[key] > amount:
        winner = key
        amount = my_dict[key]

print(f'The winner is {winner} with bid of ₹{amount}')
