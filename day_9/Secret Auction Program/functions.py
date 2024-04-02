import os
import platform


def clear_screen():
    """Очищает консоль в зависимости от операционной системы."""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def print_result(members):
    winner_name = ''
    winner_bid = 0
    for name in members:
        if members[name] > winner_bid:
            winner_name = name
            winner_bid = members[name]
    print(f"The winner is {winner_name}, with bid = {winner_bid}$")