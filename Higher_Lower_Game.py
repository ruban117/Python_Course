logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
import game_data
import random
import os
a=random.choice(game_data.data)
b=random.choice(game_data.data)
game=True
i=0
print(logo)
print(f"Compare A: {a['name']} a {a['description']} from {a['country']}")
print(vs)
print(f"Compare B: {b['name']} a {b['description']} from {b['country']}")
while game!=False:
    check=input("Who has more followers? Type 'A' or 'B': ").lower()
    if check == 'a':
        if a['follower_count']>b['follower_count']:
            os.system('cls')
            print(logo)
            i+=1
            print(f"You're right! Current score: {i}.")
            print(f"Compare A: {a['name']} a {a['description']} from {a['country']}")
            print(vs)
            b=random.choice(game_data.data)
            print(f"Compare B: {b['name']} a {b['description']} from {b['country']}")
        else:
            game=False
    elif check == 'b':
        if b['follower_count']>a['follower_count']:
            os.system('cls')
            print(logo)
            i+=1
            print(f"You're right! Current score: {i}.")
            print(f"Compare A: {b['name']} a {b['description']} from {b['country']}")
            print(vs)
            a=random.choice(game_data.data)
            print(f"Compare B: {a['name']} a {a['description']} from {a['country']}")
        else:
            game=False
os.system('cls')
print(logo)
print(f"Sorry, that's wrong. Final score: {i}")
