from cards import cards
from cards import scores
import random

def game():
    cards_amount = [51]
    player_cards = [give_card(cards_amount), give_card(cards_amount)]
    dealer_cards = [give_card(cards_amount)]
    continue_game = print_message1(player_cards, dealer_cards)
    while continue_game:
        type = input('Type "y" to get another card or type "n" to pass: ')
        if type == "y":
            player_cards.append(give_card(cards_amount))
            continue_game = print_message1(player_cards, dealer_cards)
        if type == "n":
            continue_game = False
    player_score = calcaulate_scores(player_cards)
    configure_dealer(dealer_cards, cards_amount)
    dealer_score = calcaulate_scores(dealer_cards)
    if player_score > 21:
        print("YOU ARE FUCKING LOOOZER!!!!!")
    elif player_score == 21 or dealer_score > 21:
        print("WINNER!!! WE ARE THE CHAMPIONS!!!!!")
    elif player_score > dealer_score:
        print("WINNER!!! WE ARE THE CHAMPIONS!!!!!")
    elif player_score == dealer_score:
        print("standoff!!!!!!")
    else:
        print("YOU ARE FUCKING LOOOZER!!!!!")
    print_message1(player_cards, dealer_cards)


def give_card(cards_amount):
    cards_amount_num = cards_amount[0]
    num = random.randint(0, cards_amount_num)
    cards_amount_num -= 1
    cards_amount[0] = cards_amount_num
    return cards[num]

def calcaulate_scores(cards):
    card_score = 0
    for card in cards:
        card_score += scores[card]
    return card_score


def print_message1(player_cards, dealer_cards):
    score = calcaulate_scores(player_cards)
    print(f'Your cards: {player_cards}, current score: {score}')
    print(f'Computers card is {dealer_cards}, current score: {calcaulate_scores(dealer_cards)}')
    if score >= 21:
        return False
    return True

def configure_dealer(dealer_cards, cards_amount):
    dealer_score = calcaulate_scores(dealer_cards)
    while dealer_score < 17:
        dealer_cards.append(give_card(cards_amount))
        dealer_score = calcaulate_scores(dealer_cards)
        cards_amount[0] = cards_amount[0] - 1