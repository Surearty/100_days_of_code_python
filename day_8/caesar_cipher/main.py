def encrypt(message, shift):
    new_message = ""
    for chr in message:
        if chr.isalpha():
            ch = alphabet.index(chr) + shift
            if ch > 25:
                ch = ch-26
            new_message += alphabet[ch]
        else:
            new_message += chr
    print(new_message)


alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

print(len(alphabet))

direction = input("Type '1' to encrypt, type '2' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

encrypt(text, shift)
