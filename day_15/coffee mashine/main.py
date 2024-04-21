from menu import MENU
from menu import resources


def validate_command(command):
    if command == 'report':
        print(resources)
    elif command == 'off':
        exit()
    else:
        print("NOT VALID COMMAND!!!")


def check_resources(ingredient):
    water = resources['water'] - ingredient['water']
    milk = resources['milk'] - ingredient['milk']
    coffee = resources['coffee'] - ingredient['coffee']
    if water >= 0 and milk >= 0 and coffee >= 0:
        return True
    else:
        if water < 0:
            print("Sorry there is not enough water.")
        if milk < 0:
            print("Sorry there is not enough milk.")
        if coffee < 0:
            print("Sorry there is not enough milk.")
    return False


def check_money(money, price):
    if money < price:
        print("Sorry that's not enough money. Money refunded.")
        return False
    change = money - price
    if change > resources['money']:
        print('Not enough change! Very sorry!!!')
        return False
    return True


def insert_money():
    print("please insert coins:")
    quarters = int(input('How many quarters: '))
    dimes = int(input('How many dimes: '))
    nickles = int(input('How many nickles: '))
    pennies = int(input('How many pennies: '))
    total = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    return float(total)


def make_coffee(drink, insert_money):
    resources['water'] -= MENU[drink]['ingredients']['water']
    resources['milk'] -= MENU[drink]['ingredients']['milk']
    resources['coffee'] -= MENU[drink]['ingredients']['coffee']
    change = insert_money - MENU[drink]['cost']
    resources['money'] += insert_money
    if change > 0:
        print(f'Here is ${change} dollars in change.')
        resources['money'] -= change
    print(f'Here is your {drink}. Enjoy!')


while True:
    drink = input('What would you like? (espresso/latte/cappuccino): ')
    if drink not in MENU:
        validate_command(drink)
    else:
        ingredients = MENU[drink]["ingredients"]
        price = MENU[drink]["cost"]
        print(ingredients, price)
        if check_resources(ingredients):
            money_inserted = insert_money()
            if check_money(money_inserted, price):
                make_coffee(drink, money_inserted)


