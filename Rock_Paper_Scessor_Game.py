import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choose=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print("You Choose \n")

if choose == 0 :
  print(rock)
elif choose == 1 :
  print(paper)
elif choose == 2 :
  print(scissors)
else :
  print("Invalid Input!")
  exit()

print("\nComputer Choose \n")

comp=random.randint(0,2)

if comp == 0 :
  print(rock)
elif comp == 1 :
  print(paper)
else :
  print(scissors)

if choose == 0 and comp == 1 :
  print("You Loose The Game!!")
elif choose == 0 and comp == 2 :
  print("You Win The Game!!")
elif choose == 1 and comp == 0 :
  print("You Win The Game!!")
elif choose == 1 and comp == 2 :
  print("You Loose The Game!!")
elif choose == 2 and comp == 0 :
  print("You Loose The Game!!")
elif choose == 2 and comp == 1 :
  print("You Win The Game!!")
else :
  print("Draw Game!!")