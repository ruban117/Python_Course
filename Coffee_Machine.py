#coffee machine project
import coffee_data
def calculate_dollars(q,d,n,p):
    calc=((0.25 * q)+(0.1 * d)+(0.05 * n)+(0.01 * p))
    return calc

def check_espresso(water,coffee):
    if water>50 and coffee>18:
        return True
    else:
        return False

def check_latte(water,milk,coffee):
    if water>200 and coffee>24 and milk>150:
        return True
    else:
        return False

def check_cappuccino(water,milk,coffee):
    if water>250 and coffee>24 and milk>100:
        return True
    else:
        return False

def check_ingrediants_espresso(w,co):
    if w<50 and co<18:
        print("Sorry there is not enough water and Coffee.")
    elif w<50:
        print("Sorry there is not enough water.")
    elif co<18:
        print("Sorry there is not enough coffee.")

def check_ingrediants_latte(w,mi,co):
    if w<200 and mi<150  and co<24:
        print("Sorry there is not enough water, Milk and Coffee.")
    elif w<200 and co<24:
        print("Sorry there is not enough water And Coffee.")
    elif w<200 and mi<150:
        print("Sorry there is not enough Water And Milk.")
    elif co<24 and mi<150:
        print("Sorry there is not enough Coffee And Milk.")
    elif w<200:
        print("Sorry there is not enough Water.")
    elif co<24:
        print("Sorry there is not enough Coffee.")
    elif mi<150:
        print("Sorry there is not enough Milk.")

def check_ingrediants_cappuccino(w,mi,co):
    if w<250 and mi<100  and co<24:
        print("Sorry there is not enough water, Milk and Coffee.")
    elif w<250 and co<24:
        print("Sorry there is not enough water And Coffee.")
    elif w<250 and mi<100:
        print("Sorry there is not enough Water And Milk.")
    elif co<24 and mi<100:
        print("Sorry there is not enough Coffee And Milk.")
    elif w<250:
        print("Sorry there is not enough Water.")
    elif co<24:
        print("Sorry there is not enough Coffee.")
    elif mi<100:
        print("Sorry there is not enough Milk.")

def condition(coffee_brand):
    print("Please Insert Coins")
    quaters=float(input("how many quarters?: "))
    dimes=float(input("how many dimes?: "))
    nickles=float(input("how many nickles?: "))
    pennies=float(input("how many pennies?: "))
    if calculate_dollars(quaters, dimes, nickles, pennies)<coffee_data.MENU[coffee_brand]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    else:
        n=calculate_dollars(quaters, dimes, nickles, pennies)
        change=n-coffee_data.MENU[coffee_brand]["cost"]
        print("Here is $","%.1f" %change,"in change.")
        print(f"Here is your {coffee_brand} ☕️. Enjoy!")
Water= 300
Milk= 200
Coffee= 100
Money= 0
turn_off=True
while turn_off != False:
    user_choice=input("What Do You Like? (espresso/latte/cappuccino): ").lower()
    if user_choice == 'report':
        print(f"Water={Water}ml")
        print(f"Milk={Milk}ml")
        print(f"Coffee={Coffee}ml")
        print("Money= $","%.1f" %Money)
    elif user_choice == 'espresso':
        if check_espresso(Water,Coffee):
            condition("espresso")
            Water-=coffee_data.MENU["espresso"]["ingredients"]["water"]
            Coffee-=coffee_data.MENU["espresso"]["ingredients"]["coffee"]
            Money+=coffee_data.MENU["espresso"]["cost"]
        else:
            check_ingrediants_espresso(Water,Coffee)
    elif user_choice =='latte':
        if check_latte(Water, Milk, Coffee):
            condition("latte")
            Water-=coffee_data.MENU["latte"]["ingredients"]["water"]
            Milk-=coffee_data.MENU["latte"]["ingredients"]["milk"]
            Coffee-=coffee_data.MENU["latte"]["ingredients"]["coffee"]
            Money+=coffee_data.MENU["latte"]["cost"]
        else:
            check_ingrediants_latte(Water, Milk, Coffee)
    elif user_choice == 'cappuccino':
        if check_cappuccino(Water, Milk, Coffee):
            condition("cappuccino")
            Water-=coffee_data.MENU["cappuccino"]["ingredients"]["water"]
            Milk-=coffee_data.MENU["cappuccino"]["ingredients"]["milk"]
            Coffee-=coffee_data.MENU["cappuccino"]["ingredients"]["coffee"]
            Money+=coffee_data.MENU["cappuccino"]["cost"]
        else:
            check_ingrediants_cappuccino(Water, Milk, Coffee)
    elif user_choice == 'off':
        print("Thank You For Using Ruban's Coffee Machine Again Come!!")
        turn_off=False
    else:
        print("Please Choice Correct Input")