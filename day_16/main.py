from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_mashine import MoneyMachine

cof_menu = Menu()
cof_maker = CoffeeMaker()
mon_machine = MoneyMachine()
is_on = True
while is_on:
    options = cof_menu.get_items()
    drink = input(f'What would you like? {options}: ')
    if drink == 'off':
        is_on = False
    elif drink == 'report':
        cof_maker.report()
        mon_machine.report()
    else:
        drink = cof_menu.find_drink(drink)
        if drink is not None and cof_maker.is_resource_sufficient(drink):
            if mon_machine.make_payment(drink.cost):
                cof_maker.make_coffee(drink)
