print("Welcome to python pizza delivery:")
rate=0
size=input("Please enter the size of the pizza: s for small, m for medium and l for large: \n")


if size == "s":
    rate = 15
elif size == "m":
    rate = 20
elif size == "l":
    rate = 25
else:
    print("you typed invalid input:")

pep=input("Would you like peporani: y for yes and n for no: \n")
extra_cheese=input("Would you like extra cheese: y for yes and n for no: \n")

if pep == "y":
    if size == 's':
        rate += 2
    else:
        rate +=3

if extra_cheese == "y":
    rate += 1
print(f"the rate of pizza is {rate}")
