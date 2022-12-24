def turn_right():
    turn_left()
    turn_left()
    turn_left()
def Same_Thing():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
#while at_goal()!=True :
#   Same_Thing()

while not at_goal():
    Same_Thing()

