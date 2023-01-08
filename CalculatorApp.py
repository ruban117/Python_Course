import os
import art_Calculator_App
#addition
def addition(a, b):
    if a == "" or b == "":
        return "You have to input something!"
    return a + b


#subtraction
def subtraction(a, b):
    if a == "" or b == "":
        return "You have to input something!"
    return a - b


#multiplication
def multiplication(a, b):
    if a == "" or b == "":
        return "You have to input something!"
    return a * b


#divition
def divition(a, b):
    if a == "" or b == "":
        return "You have to input something!"
    return a / b


operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": divition,
}

def calculator():
    print(art_Calculator_App.logo)
    num1 = float(input("Enter the first number: "))
    print("\n")

    for f in operations:
        print(f)
    print("\n")

    symbol = input("Pick an operation from the line above: ")
    print("\n")

    num2 = float(input("Enter the second number: "))
    print("\n")

    function = operations[symbol]

    answer = function(num1, num2)

    print(f"{num1} {symbol} {num2} = {answer}")

    end = True
    while end:
        cont = input(f"\nType 'y' to continue adding with {answer} or Type 'n' to start a new calculation or type 'c' to shutdown: ").lower()
        if cont == 'y' or cont == 'yes':
            end = True
        elif cont=='c' or cont == 'close':
            print("\n*****************Goodbye!******************************")
            break
        elif cont == 'n' or cont == 'no':
            end = False
            os.system('cls')
            calculator()
        print("\n")
        for f in operations:
            print(f)
        print("\n")
        symbol = input("Pick an operation: ")
        print("\n")
        
        num3 = float(input("Enter the another number: "))
        print("\n")
        
        function = operations[symbol]
        
        answer2 = function(answer, num3)
        
        print(f"{answer} {symbol} {num3} = {answer2}")
calculator()
