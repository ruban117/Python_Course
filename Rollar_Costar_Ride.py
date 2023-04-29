print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride into the rollarcostar")
    age = int(input("Enter your age: "))
    if age <= 12:
        bill += 5
        print("You have to pay $5")
    elif age <= 18:
        bill += 7
        print("You have to pay $7")
    elif age >= 45 and age <= 55:
        bill += 0
        print("You do not have to pay.")
    else:
        bill += 12
        print("You have to pay $12")
        want_pic = input("Do you want pictures? 'Y' or 'N' ")
        if want_pic == 'Y':
            bill += 3
            print(f"Your final bill is ${bill}")
        else:
            print(f"Your final bill is ${bill}")
else :
  print("Sorry, you can't ride into the rollarcoster!")
