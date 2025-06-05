print("Welcome to python pizza delivery:")
rate=0
size=input("Please enter the size of the pizza: s for small, m for medium and l for large:")
pep=input("Would you like peporani: y for yes and n for no")
extra_cheese=input("Would you like extra cheese: y for yes and n for no")
if size == "s":
    rate = 15
    if pep == "y":
        rate += 2
    if extra_cheese == "y":
        rate += 1

elif size == "m":
    rate = 20
    if pep == "y":
        rate += 3
    if extra_cheese == "y":
        rate += 1



elif size == "l":
    rate = 25
    if pep == "y":
        rate += 3
    if extra_cheese == "y":
        rate += 1

else:
    print("you typed invalid input:")

print(f"the rate of pizza is {rate}")
