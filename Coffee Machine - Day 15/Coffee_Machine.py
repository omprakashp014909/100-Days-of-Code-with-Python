import os

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


Hot_brew_emoji = "☕"

def display_report():
    """Displays available Resources"""
    print(f"Water: {resources.get('water')}ml")
    print(f"Milk: {resources.get('milk')}ml")
    print(f"Coffee: {resources.get('coffee')}g")
    print(f"Money: ${round(resources.get('money'),2)}")

def process_coins(quarters, dimes,nickles, pennies):
    """counts the inserted coins and returns the total"""
    return  quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*.01
    
def return_change(extra_amount):
    """Takes extra money as an input and Returns the change."""
    amount = extra_amount
    if amount == 0:
        return 0
    
    print(f"\nHere is ${round(amount,2)} dollars in change.")
    if amount>=0.25:
        quarters = amount//0.25
        amount -= quarters*0.25
        print(f'quarters: {quarters}')

    if amount>= 0.1:
        dimes = amount//0.1
        amount -= dimes*0.1
        print(f"dimes: {dimes}")
    
    if amount >= 0.05:
        nickles = amount//0.05
        amount -= nickles*0.05
        print(f"nickles: {nickles}")

    pennies = amount // 0.01
    print(f"pennies: {pennies}")
    

# TODO: checks available ingredients are sufficient for making coffee
def check_ingredients(order):
    """ Chekcs available resources for brewing the coffee and retruns True for sufficient resources else returns what is lacking"""

    for item in MENU[order]["ingredients"]:
        if resources[item]<MENU[order]["ingredients"].get(item,0):
            print(f"Sorry there is not enough {item}.")
            return
    
    return True
    
# TODO: Deduct ingredients after brewing the coffee
def deduct_ingredients(order):
    for item in MENU[order]["ingredients"]:
        resources[item] = resources.get(item) - MENU[order]["ingredients"].get(item,0)

machine_on = True
while machine_on: 
    #  TODO: Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
    order = input(f"What would you like? (espresso/latte/cappuccino){Hot_brew_emoji}:").strip().lower()

    #  TODO:Turning machine off
    if order == "off":
        machine_on = False
    elif order == "report":
        display_report()
    
    # TODO: Checking do we have sufficient ingredients for brewing the coffee 
    elif check_ingredients(order) == True:
        # TODO: Request for inserting coins
        print("Please insert coins as follows:")
        inserted_money = process_coins(int(input("quarters:")), int(input("dimes:")), int(input("nickles:")), int(input("pennies:")))
        
        # checking for required money for brewing order and accordingly updating resources
        if inserted_money >= MENU[order].get("cost"):
            # TODO: Updating money to resources
            resources["money"] = round(resources.get("money") + inserted_money,2)
            # Deduct the used ingredients form the resources
            deduct_ingredients(order)
            # return change
            return_change(inserted_money - MENU[order].get("cost"))
            print(f"Here is your {order.title()} {Hot_brew_emoji}. Enjoy!")
        else:
            print("Sorry that's not enough money. Money returned.")

    # clear screen
    os.system('cls') 
    