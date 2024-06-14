MENU = {
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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resources(ingredients):
    for i in ingredients:
        if ingredients[i] > resources[i]:
            print(f'not enough resources for {i}.')
        else:
            return True

def check_payment(quarters,dimes,nickels,pennies):
    a = quarters * .25
    b = dimes * .1
    c = nickels * .05
    d = pennies * .01
    Total = round(a + b + c + d,2)
    return Total

def make_drink(ingredients):
    for i in ingredients:
        resources[i] -= ingredients[i]


def make_change(total,drink):
    change = float(total - drink)
    return f'your change is {change}'



machine_on = True
while machine_on != False:
    choice = input('What would you like? (espresso/latte/cappuccino):')
    if choice == "off":
        machine_on = False
    elif choice == "report":
        for item in resources.items():
            print(item)
    else:
        drink = MENU[choice]
        check_resources(drink['ingredients'])
        quarters = int(input("how many quarters?"))
        dimes = int(input("How many dimes?"))
        nickels = int(input("How many nickels?"))
        pennies = int(input("how many pennies?"))
        if check_payment(quarters,dimes,nickels,pennies) < drink['cost']:
            print(f"Not enough money")
        else:
            payment = check_payment(quarters,dimes,nickels,pennies)
            make_drink(drink['ingredients'])
            make_change(payment,drink['cost'])
            profit += drink['cost']
            print(f'Enjoy your {choice}')


