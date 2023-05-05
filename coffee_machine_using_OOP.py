#coffee machine using oop
class MenuData:
    def __init__(self):
        self.MENU = {
            "espresso": {
                "ingredients": {
                    "water": 50,
                    "coffee": 18,
                },
                "cost": 1.5,
            },
            "latte": {
                "ingredients": {
                    "water": 200,
                    "milk": 150,
                    "coffee": 24,
                },
                "cost": 2.5,
            },
            "cappuccino": {
                "ingredients": {
                    "water": 250,
                    "milk": 100,
                    "coffee": 24,
                },
                "cost": 3.0,
            }
        }

    def check_espresso(self,water, coffee):
        if water >= self.MENU["espresso"]["ingredients"]["water"] and coffee >= self.MENU["espresso"]["ingredients"]["coffee"]:
            return True
        else:
            return False


    def check_latte(self,water, milk, coffee):
        if water >= self.MENU["latte"]["ingredients"]["water"] and coffee >= self.MENU["latte"]["ingredients"]["coffee"] and milk > self.MENU["latte"]["ingredients"]["milk"]:
            return True
        else:
            return False


    def check_cappuccino(self,water, milk, coffee):
        if water >= self.MENU["cappuccino"]["ingredients"]["water"] and coffee >=self.MENU["cappuccino"]["ingredients"]["coffee"] and milk > self.MENU["cappuccino"]["ingredients"]["milk"]:
            return True
        else:
            return False


    def check_ingrediants_espresso(self,w, co):
        if w < self.MENU["espresso"]["ingredients"]["water"] and co < self.MENU["espresso"]["ingredients"]["coffee"]:
            print("Sorry there is not enough water and Coffee.")
        elif w < self.MENU["espresso"]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
        elif co < self.MENU["espresso"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")


    def check_ingrediants_latte(self,w, mi, co):
        if w < self.MENU["latte"]["ingredients"]["water"] and mi < self.MENU["latte"]["ingredients"]["milk"] and co < self.MENU["latte"]["ingredients"]["coffee"]:
            print("Sorry there is not enough water, Milk and Coffee.")
        elif w < self.MENU["latte"]["ingredients"]["water"] and co < self.MENU["latte"]["ingredients"]["coffee"]:
            print("Sorry there is not enough water And Coffee.")
        elif w < self.MENU["latte"]["ingredients"]["water"] and mi < self.MENU["latte"]["ingredients"]["milk"]:
            print("Sorry there is not enough Water And Milk.")
        elif co < self.MENU["latte"]["ingredients"]["coffee"] and mi < self.MENU["latte"]["ingredients"]["milk"]:
            print("Sorry there is not enough Coffee And Milk.")
        elif w < self.MENU["latte"]["ingredients"]["water"]:
            print("Sorry there is not enough Water.")
        elif co < self.MENU["latte"]["ingredients"]["coffee"]:
            print("Sorry there is not enough Coffee.")
        elif mi < self.MENU["latte"]["ingredients"]["milk"]:
            print("Sorry there is not enough Milk.")


    def check_ingrediants_cappuccino(self,w, mi, co):
        if w < self.MENU["cappuccino"]["ingredients"]["water"] and mi < self.MENU["cappuccino"]["ingredients"]["milk"] and co < self.MENU["cappuccino"]["ingredients"]["coffee"]:
            print("Sorry there is not enough water, Milk and Coffee.")
        elif w < self.MENU["cappuccino"]["ingredients"]["water"] and co < self.MENU["cappuccino"]["ingredients"]["coffee"]:
            print("Sorry there is not enough water And Coffee.")
        elif w < self.MENU["cappuccino"]["ingredients"]["water"] and mi < self.MENU["cappuccino"]["ingredients"]["milk"]:
            print("Sorry there is not enough Water And Milk.")
        elif co < self.MENU["cappuccino"]["ingredients"]["coffee"] and mi < self.MENU["cappuccino"]["ingredients"]["milk"]:
            print("Sorry there is not enough Coffee And Milk.")
        elif w < self.MENU["cappuccino"]["ingredients"]["water"]:
            print("Sorry there is not enough Water.")
        elif co < self.MENU["cappuccino"]["ingredients"]["coffee"]:
            print("Sorry there is not enough Coffee.")
        elif mi <self.MENU["cappuccino"]["ingredients"]["milk"] :
            print("Sorry there is not enough Milk.")
class View_Resources:
    def __init__(self):
        self.resources = {
        "Water": 300,
        "Milk": 200,
        "Coffee": 100,
        "Money" : 0
    }
    def print_resources(self):
        print("Water=",self.resources["Water"],"ml")
        print("Milk=",self.resources["Milk"],"ml")
        print("Coffee=",self.resources["Coffee"],"ml")
        print("Money=$",self.resources["Money"])
class CurrencyCalculator:
    md=MenuData()
    vr=View_Resources()
    def __init__(self):
        self.quarters=0.25
        self.dimes=0.1
        self.nickles=0.05
        self.pennies=0.01
    def calculate_dollars(self,q,d,n,p):
        calc=((self.quarters * q)+(self.dimes * d)+(self.nickles * n)+(self.pennies * p))
        return calc
    def condition(self,coffee_brand):
        print("Please Insert Coins")
        quaters=float(input("how many quarters?: "))
        dimes=float(input("how many dimes?: "))
        nickles=float(input("how many nickles?: "))
        pennies=float(input("how many pennies?: "))
        if self.calculate_dollars(quaters, dimes, nickles, pennies)<md.MENU[coffee_brand]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
        else:
            if coffee_brand == 'espresso':
                n=self.calculate_dollars(quaters, dimes, nickles, pennies)
                change=n-md.MENU[coffee_brand]["cost"]
                vr.resources['Water']-=md.MENU["espresso"]["ingredients"]["water"]
                vr.resources['Coffee']-=md.MENU["espresso"]["ingredients"]["coffee"]
                vr.resources['Money']+=md.MENU["espresso"]["cost"]
                print("Here is $","%.1f" %change,"in change.")
                print(f"Here is your {coffee_brand} ☕️. Enjoy!")
            else:
                n=self.calculate_dollars(quaters, dimes, nickles, pennies)
                change=n-md.MENU[coffee_brand]["cost"]
                vr.resources['Water']-=md.MENU[coffee_brand]["ingredients"]["water"]
                vr.resources['Milk']-=md.MENU[coffee_brand]["ingredients"]["milk"]
                vr.resources['Coffee']-=md.MENU[coffee_brand]["ingredients"]["coffee"]
                vr.resources['Money']+=md.MENU[coffee_brand]["cost"]
                print("Here is $","%.1f" %change,"in change.")
                print(f"Here is your {coffee_brand} ☕️. Enjoy!")
                


md=MenuData()
cc=CurrencyCalculator()
vr=View_Resources()
turn_off=True
while turn_off != False:
    user_choice=input("What Do You Like? (espresso/latte/cappuccino): ").lower()
    if user_choice == 'report':
        vr.print_resources()
    elif user_choice == 'espresso':
        if md.check_espresso(vr.resources['Water'],vr.resources['Coffee']):
            cc.condition("espresso")
        else:
            md.check_ingrediants_espresso(vr.resources['Water'],vr.resources['Coffee'])
    elif user_choice =='latte':
        if md.check_latte(vr.resources['Water'], vr.resources['Milk'], vr.resources['Coffee']):
            cc.condition("latte")
        else:
            md.check_ingrediants_latte(vr.resources['Water'], vr.resources['Milk'], vr.resources['Coffee'])
    elif user_choice == 'cappuccino':
        if md.check_cappuccino(vr.resources['Water'], vr.resources['Milk'], vr.resources['Coffee']):
            cc.condition("cappuccino")
        else:
            md.check_ingrediants_cappuccino(vr.resources['Water'], vr.resources['Milk'], vr.resources['Coffee'])
    elif user_choice == 'off':
        print("Thank You For Using Ruban's Coffee Machine Again Come!!")
        turn_off=False
    else:
        print("Please Choice Correct Input")
