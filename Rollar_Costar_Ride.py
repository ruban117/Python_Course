print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride into rollarcoster.")
    age = int(input("Enter your age: "))
    if age <= 12:
        bill = 5
        print("Please Pay $5")
    elif age <= 18:
        bill = 7
        print("Please pay $7")
    elif age > 18:
        bill = 12
        print("Please pay $12")
        want_photo = input("Do you want some photos?: 'Y' or 'N' ")
        if want_photo == 'Y':
            bill += 3
            print(f"So your total bill is {bill}")
else:
    print("Sorry, you can't ride into the rollarcoster!")
