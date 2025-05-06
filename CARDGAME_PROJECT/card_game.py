# Code for the card game
# We are using a small deck of cards for simplicity
# The game has 16 rounds, and the player with the most points wins

import random

SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
VALUES = list(range(1, 11)) + ["Jack", "Queen"]
# This helps define the cards in the deck and their ranks
# 2 is the weakest, and Queen is the strongest (Kings are not used)

def card_value(card):
    """Normalize face cards to numeric values for comparison."""
    if card.value == "Jack":
        return 11
    elif card.value == "Queen":
        return 12
    else:
        return card.value
# This function assigns a number to face cards for comparing their strength

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"
    # This class represents a single card in the deck

class Deck:
    def __init__(self):
        # Build and shuffle a 48-card deck (no Kings)
        self.cards = [Card(s, v) for s in SUITS for v in VALUES]
        random.shuffle(self.cards)
    # This creates and mixes up the deck at the start

    def deal(self, count):
        """Deal 'count' cards (or fewer if deck is low)."""
        hand = []
        for _ in range(count):
            if self.cards:
                hand.append(self.cards.pop())
        return hand

    def __len__(self):
        return len(self.cards)
# This class handles the deck of cards and how we draw from it

def main():
    deck = Deck()
    p1_score = 0
    p2_score = 0
    round_num = 1

    while round_num <= 16 and len(deck) >= 2:
        print(f"\n--- Round {round_num} ---")
        card1, card2 = deck.deal(2)
        print("Player 1 drew:", card1)
        print("Player 2 drew:", card2)

        v1, v2 = card_value(card1), card_value(card2)

        if v1 > v2:
            p1_score += 1
            print("→ Player 1 wins the round.")
        elif v2 > v1:
            p2_score += 1
            print("→ Player 2 wins the round.")
        else:
            print("→ It's a tie. No points awarded.")

        round_num += 1

    print("\n--- Final Scores ---")
    print("Player 1:", p1_score)
    print("Player 2:", p2_score)


    if (p1_score == 16 and p2_score == 0):
        print("Player 2 shot the moon! They score 17 points and win.")
    elif (p2_score == 16 and p1_score == 0):
        print("Player 1 shot the moon! They score 17 points and win.")
    else:
        if p1_score > p2_score:
            print("Player 1 wins!")
        elif p2_score > p1_score:
            print("Player 2 wins!")
        else:
            print("It's a tie!")

if __name__ == "__main__":
    main()