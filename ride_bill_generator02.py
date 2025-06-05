print("welcome to the ride:")
height = int(input("How tall are you?\n"))
age = int(input("How old are you?\n"))
bill=0
if height > 120:
    print("You can ride")
    if age <=12 :
        bill=5
        print("Childeren's ticket: $5")
    elif age <= 18:
        bill=7
        print("Youth's ticet: $7")
    else:
        bill=12
        print("Adult's ticket: $12")

    photo=input("do you want photograph of the ride it costs $3 type y for yes or n for no:\n")
    if photo == "y":
        bill += 3
        print(f"Your final bill is: ${bill}")
    else:
        print(f"Your final bill is: ${bill}")

else:
    print("You can not ride")