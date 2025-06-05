print("Welcome to the tip calculator!")

bill=float(input("What wos the total bill? $"))

tip=int(input("How much tip would you like to give? 10, 12, or 15?"))

number_of_people=int(input("How many people to split the bill?"))

total_bill= bill + bill * (tip/100)

contry=round(total_bill/number_of_people,2)

print("Each persion should pay: "+str(contry))
