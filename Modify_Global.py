enemies=1

def increase_enemies():
    global enemies
    enemies+=1
    print(f"The enemies are inside function {enemies}")

print(f"The enemies are outside function {enemies}")
increase_enemies()