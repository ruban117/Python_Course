print(''' / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  ''')
import random
numbers=[i for i in range(1,101)]
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
num=random.choice(numbers)
def main_work(s,st):
    for i in range(s,st,-1):
        print(f"You have {i} attempts remaining to guess the number.")
        guess=int(input("Make a guess: "))
        if guess == num:
            print(f"You got it! The answer was {num}.")
            break
        elif guess > num:
            print("Too high.")
        elif guess < num:
            print("Too Low")
    else:
        print("You've run out of guesses, you lose.")
diff=input("Choose a difficulty. Type 'easy' or 'hard':- ").lower()
if diff == 'easy':
    main_work(10,0)
elif diff == 'hard':
    main_work(5,0)
else:
    print("Wrong Input")