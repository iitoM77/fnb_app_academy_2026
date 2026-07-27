
#ask user how many kilometers they wanna drive & they price of fuel
kilos = int(input("Please enter the distance you want to travel in km: "))
fuel_price = float(input("How many is the price of 1 litre of fuel: R"))

#calculate the litres needed for the trip at 1 litre per 10km traveled
liters_needed = kilos / 10

#calculate the total cost of the trip
total_cost = float(liters_needed) * fuel_price

#display how much it will cost for the trip with the total cost rounded to 2 decimals
print(f"Dear sir/Madam, It will cost you R{str(round(total_cost,2))} to travel {str(kilos)} Km. Thank you & have a safe trip")