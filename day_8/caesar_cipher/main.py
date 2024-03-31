from art import logo
from caesar import caesar

print(logo)

while type != "no":
    direction = int(input("Type '1' to encrypt, type '2' to decrypt:\n"))
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)
    type = input("Type 'yes' to continue or 'no' to exit\n")
