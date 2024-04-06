import random

def try_to_guess(number):
    if number == guess_number:
        print("YOU WIN THE GAME!!!")
        return True
    elif number < guess_number:
        print('Too low')
    else:
        print('Too high!')
    return False

print('Welcome to the number guessing game!!!')
print('I`m thinking of a number between 1 and 100')
guess_number = random.randint(1,100)
win_game = False
difficult = input("Choose a difficulty, type 'easy' or 'hard': ")
attempts = 10 if difficult == 'easy' else 5

while attempts > 0 and win_game == False:
    print(f'You have {attempts} attempts remaining to guess the number')
    number = int(input('Make a guess: '))
    win_game = try_to_guess(number)
    attempts -= 1
if win_game == False:
    print('You looose the game')
    print(f'i guess {guess_number}')


