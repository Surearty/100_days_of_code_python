import random
word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the word_list and assign it to a
#  variable called chosen_word.

# Ask the user to guess a letter and assign their answer to a
# variable called guess. Make guess lowercase.

# Check if the letter the user guessed (guess) is one of the
# letters in the chosen_word.

chosen_word = word_list[random.randint(0, len(word_list)-1)].lower()
guess = input('guess a letter:').lower()
for ch in chosen_word:
    if guess == ch:
        print('Right')
    else:
        print('Wrong')
