################## Coffee Machine ##############################

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
}



def customer_order():
    choice = input("What would you like? (espresso/latte/cappuccino):")
    return choice

money = 0


def print_report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: ${money}")


def check_resources(coffee):
    for item in MENU[coffee]['ingredients']:
        if MENU[coffee]['ingredients'][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# TODO: 5. Process coins.
def calculate_coin(coffee_cost):
    money_paid = (0.25 * coin_quarters) + (0.10 * coin_dimes) + (0.05 * coin_nickels) + (0.01 * coin_pennies)
    if money_paid >= coffee_cost:
        print(f"The total cost is ${coffee_cost}, Customer gave: ${money_paid}")
        change = round(money_paid - coffee_cost, 2)
        print(f"Here is ${change} in change.")
        return True, coffee_cost
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False, 0


while True:
    coffee_type = customer_order()

    if coffee_type == 'off':
        print('Goodbye!')
        break

    if coffee_type == 'report':
        print_report()
        continue

    if coffee_type not in ["espresso", "latte", "cappuccino"]:
        print("Invalid choice. Please try again.")
        continue

    if not check_resources(coffee_type):
        continue

    print("Please insert coins.")
    coin_quarters = int(input("how many quarters?: "))
    coin_dimes = int(input("how many dimes?: "))
    coin_nickels = int(input("how many nickels?: "))
    coin_pennies = int(input("how many pennies?: "))

    is_sufficient, cost = calculate_coin(MENU[coffee_type]['cost'])

    if is_sufficient:
        money += cost
        for item in MENU[coffee_type]['ingredients']:
            resources[item] -= MENU[coffee_type]['ingredients'][item]
        print(f"Here is your {coffee_type} ☕. Enjoy!")
