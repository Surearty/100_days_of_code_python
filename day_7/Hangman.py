import random
word_list = ["aardvark", "baboon", "camel"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = 6
chosen_word = random.choice(word_list).lower()
print(f'Pssst, the solution is {chosen_word}.')
your_ans = ['_'] * len(chosen_word)
game = True
while (''.join(your_ans) != chosen_word and lives > 0):
    guess = input('guess a letter:').lower()
    guess_num = 0
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            your_ans[i] = guess
            guess_num += 1
    if guess_num == 0:
        lives -= 1
        print(stages[lives])
        print(your_ans)
        if lives == 0:
            game = False
            break
    else:
        print(your_ans)
if game:
    print('YOU WIN!')
else:
    print('YOU LOOOSE!')
