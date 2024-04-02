from art import logo
from functions import clear_screen
from functions import print_result

print(logo)
print("Welcome to the secret auction programm")

members = {}
another = "y"
while another != "n":
    name = input("What is your name? ")
    bid = int(input("What`s your bid? $"))
    members[name]= bid
    another = input('Are there another bidders? type "y" or "n": ')
    clear_screen()
print_result(members)