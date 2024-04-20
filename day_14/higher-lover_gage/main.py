from game_data import data
import random
from art import vs


score = 0
win = 1

while win == 1 and score < 50:
    person1_num = random.randint(0, len(data)-1)
    person1 = data.pop(person1_num)
    person2_num = random.randint(0, len(data)-1)
    person2 = data.pop(person2_num)
    correct_ans = 'A' if person1['follower_count'] > person2['follower_count'] else 'B'
    print(f'Compare A: {person1['name']}, {person1['description']}, from {person1['country']}')
    print(vs)
    print(f'Compare B: {person2['name']}, {person2['description']}, from {person2['country']}')
    player_ans = input()
    if player_ans == correct_ans:
        score += 1
        print(f"Correct answer!!!! your score = {score}")
    else:
        win = 0
if win == 0:
    print(f'YOU LOOOSE!!!! Your score is {score}')
elif score == 50:
    print('YOU WIN THE GAME')

