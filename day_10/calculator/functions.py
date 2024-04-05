import os
import platform


def clear_screen():
    """Очищает консоль в зависимости от операционной системы."""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multyply(a, b):
    return a * b


def divide(a, b):
    return a / b


operations = {"+": add, "-": subtract, "*": multyply, "/": divide}


def calculate():
    num1 = float(input("Whats the first number? "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operatyon: ")
        num2 = float(input("Whats the second number? "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        type = input(
            f"type 'y' to continue calculating with {answer}, "
            "type 'n' to exit or type 'r' to restart calculating: "
        )
        if type == "n":
            should_continue = False
        elif type == "y":
            num1 = answer
        else:
            clear_screen()
            calculate()