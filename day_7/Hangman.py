import random
from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list

print(logo)
lives = 6
chosen_word = random.choice(word_list).lower()
print(f'Pssst, the solution is {chosen_word}.')
your_ans = ['_'] * len(chosen_word)
game = True
while (''.join(your_ans) != chosen_word and game):
    guess = input('guess a letter:').lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            your_ans[i] = guess
    if guess not in chosen_word:
        lives -= 1
        print(your_ans)
        print(stages[lives])
        if lives == 0:
            game = False
    else:
        print(your_ans)
if game:
    print('YOU WIN!')
else:
    print('YOU LOOOSE!')
