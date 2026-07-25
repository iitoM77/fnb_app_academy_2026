# I will first have a greeting message that also asks for the customer's name
name = input("Please enter your name: ")
# now the customer must choose the artist from the list of artists displayed
artists = ["1. Nasty C", "2.A-reece", "3.Blxckie", "4.6lack"]
for artist in artists:
    print(artist)
choice = input("please pick an artist name: ")
#now I have added an option to select amount of tickets to buy
tickets = input("How many tickets do you wanna purchase?: ")
# this here is the final print message 
print(f"Hello, {name}! you have successfully bought {tickets} tickets to see {choice} . Thank you and have a good day")