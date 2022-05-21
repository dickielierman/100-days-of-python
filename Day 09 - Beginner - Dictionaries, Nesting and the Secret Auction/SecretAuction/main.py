import art
from my_funcs import pause, my_input, clear
auction_list = {}


def save_bid(name, price):
    auction_list[name] = price


def get_results(auction_list):
    highest_bid = 0
    highest_bidder = ''
    for person in auction_list:
        if auction_list[person] > highest_bid:
            highest_bid = auction_list[person]
            highest_bidder = person
    print(highest_bidder.capitalize() + ' is the highest bidder, with a bid of ' + "${:,.2f}".format(highest_bid))


yes_or_no = ['y', 'yes', 'n', 'no']

complete = False
print(art.logo)
ready = my_input('Are you ready to get started? ', yes_or_no)
if ready in ['y', 'yes']:
    clear()
    while not complete:
        name = my_input('What is the name for this entry? ')
        bid = float(my_input('What is the bid? $'))
        save_bid(name, bid)
        more_bidders = my_input("Are there more bidders who would like to participate? ", yes_or_no).lower()

        if more_bidders in ['n', 'no']:
            complete = True
            clear()
            break
        else:
            clear()
    get_results(auction_list)
