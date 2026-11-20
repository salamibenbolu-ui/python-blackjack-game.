# Creating a blackjack game

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# select card randomly
def deal_card():
    picked_card = random.choice(cards)
    return picked_card


player_cards = []
dealer_cards = []

# Assign to cards randomly to player
player_cards.append(deal_card())
player_cards.append(deal_card())

# Assign two cards randomly to dealer
dealer_cards.append(deal_card())
dealer_cards.append(deal_card())


# calculate total value of cards held
def calculate_score(card_list):
    score = sum(card_list)

    while score > 21 and 11 in card_list:
        card_list[card_list.index(11)] = 1
        score = sum(card_list)
    return score


print(f"Player's cards: {player_cards}")
print(f"Player's score: {calculate_score(player_cards)}")

print(f"Dealer's card: {dealer_cards[0]}")
print("Dealer's second card will stay hidden")

player_busted = False
while True:
    # check player current score
    choice = input("Do you want to HIT or STAND? ").strip().lower()
    if choice == "hit":
        player_cards.append(deal_card())

        print(f"Player's cards: {player_cards}")
        print(f"Score: {calculate_score(player_cards)}")

        if calculate_score(player_cards) > 21:
            print("Player loses")
            player_busted = True
            break

    elif choice == "stand":
        break

    else:
        print("Invalid choice. Please enter HIT or STAND")

# checks if player card exceeds 21
if player_busted:
    print("Dealer wins")

else:
    print(f"Dealer's cards: {dealer_cards}")
    print(f"Dealer's score: {calculate_score(dealer_cards)}")

    while calculate_score(dealer_cards) < 17:
        dealer_cards.append(deal_card())
        print(f"Dealer draws: {dealer_cards[-1]}")
        print(f"Dealer's score: {calculate_score(dealer_cards)}")

    if calculate_score(dealer_cards) > 21:
        print("Player wins")
    elif calculate_score(player_cards) > calculate_score(dealer_cards):
        print("Player wins")
    elif calculate_score(dealer_cards) > calculate_score(player_cards):
        print("Dealer wins")
    else:
        print("It is a Tie")
