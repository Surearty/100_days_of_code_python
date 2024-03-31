from alphabet import alphabet


def caesar(message, shift, direction):
    new_message = ""
    if shift > 26:
        shift = shift % 26
    if direction == 2:
        shift = -shift
    for chr in message:
        if chr.isalpha():
            ch = alphabet.index(chr) + shift
            if ch > 25:
                ch = ch - 26
            elif ch < 0:
                ch = 26 + ch
            new_message += alphabet[ch]
        else:
            new_message += chr
    print(new_message)
