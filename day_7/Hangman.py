import random
word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the word_list and assign it to a
#  variable called chosen_word.

# Ask the user to guess a letter and assign their answer to a
# variable called guess. Make guess lowercase.

# Check if the letter the user guessed (guess) is one of the
# letters in the chosen_word.

chosen_word = random.choice(word_list).lower()
print(f'Pssst, the solution is {chosen_word}.')
your_ans = ['_'] * len(chosen_word)
while (''.join(your_ans) != chosen_word):
    guess = input('guess a letter:').lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            your_ans[i] = guess
            print(your_ans)

