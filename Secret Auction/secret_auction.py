print("Welcome to the secret auction\n")

bidders_information = {}

while True:
    user_input = input("Do you want you to add a bidder? Yes or No : ")

    if user_input.lower() == 'no':
        break
    elif user_input.lower() == 'yes' or user_input.lower() == 'y':
        user_name = input("Bidder's Name : ")
        user_bid  = input("Bid           : ")
    else :
        print("Invalid Input!")
        continue
    bidders_information.update({user_name : user_bid})

highest_bid = 0
highest_bidder = ""

for key,value in bidders_information.items():
    print(highest_bid)
    if int(value) > int(highest_bid):
        highest_bid = value
        highest_bidder = key
        print(f"{value, key}")
    
print(f"Higest Bidder : {highest_bidder}, highest Bid : {highest_bid}")
