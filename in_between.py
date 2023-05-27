import random


class In_Between():

    def __init__(self):
        self.card_1 = []
        self.card_2 = []
        self.card_3 = []

    def get_cards(self):
        # Define the ranks, suits, and values
        ranks = ['A', '2', '3', '4', '5', '6', '7',
                 '8', '9', '10', 'J', 'Q', 'K']
        suits = ['♠', '♥', '♦', '♣']
        values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                  '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}

        # Create the deck of cards
        deck_cards = {}
        for suit in suits:
            for rank in ranks:
                card = f'{rank} {suit}'
                deck_cards[card] = values[rank]

        for i in range(1, 4):
            random_card = random.choice(list(deck_cards.items()))
            setattr(self, f'card_{i}', random_card)

    def game_info(self):
        # Print Game
        print('''"In Between Card Game" by Lokodata

Rules:
1. You will be given 2 cards
2. If the set of cards have the same rank, you have 3 choices
    [1] Higher : You guess that the 3rd card is higher than your cards 
    [2] Lower : You guess that the 3rd card is lower than your cards 
    [3] Fold : If you don't want to guess, you can fold and get a new set of cards
3. If cards are not the same rank, you have 2 choices
    [1] In Between : You guess that the 3rd card is in between your cards 
    [2] Fold : If you don't want to guess, you can fold and get a new set of cards
4. If you guess correctly, you will be given a point and you will be given a new set of cards
5. If you guess incorrectly, game ends and you will see your score
        ''')

    def check_cards(self):
        # Check if cards are the same rank
        return self.card_1[1] == self.card_2[1]

    def run_game(self):

        scores = 0

        while True:
            self.get_cards()

            print(f"Your cards are {self.card_1[0]} and {self.card_2[0]}")

            if self.check_cards():
                choice = input("""
[1] Higher
[2] Lower
[3] Fold
[4] Quit

""")

                if choice == '1':
                    if self.card_3[1] > self.card_1[1]:
                        scores += 1
                        print(f"Your card is {self.card_3[0]}")
                        print("Your guess is correct. Keep it up!")
                    else:
                        print(f"Your card is {self.card_3[0]}")
                        print(f"Bad luck! Your final scores are {scores}")
                        break
                elif choice == '2':
                    if self.card_3[1] < self.card_1[1]:
                        scores += 1
                        print(f"Your card is {self.card_3[0]}")
                        print("Your guess is correct. Keep it up!")
                    else:
                        print(f"Your card is {self.card_3[0]}")
                        print(f"Bad luck! Your final scores are {scores}")
                        break
                elif choice == '3':
                    self.get_cards()
                    continue
                elif choice == '4':
                    print("Thanks for playing!")
                    break

            else:
                choice = input("""
[1] In Between
[2] Fold
[3] Quit

""")
                # check if card 1 is higher than card 2
                if self.card_1[1] > self.card_2[1]:
                    higher = self.card_1[1]
                    lower = self.card_2[1]
                else:
                    higher = self.card_2[1]
                    lower = self.card_1[1]

                if choice == '1':
                    if lower < self.card_3[1] < higher:
                        scores += 1
                        print(f"Your card is {self.card_3[0]}")
                        print("Your guess is correct. Keep it up!")
                    else:
                        print(f"Your card is {self.card_3[0]}")
                        print(f"Bad luck! Your final scores are {scores}")
                        break
                elif choice == '2':
                    self.get_cards()
                    continue
                elif choice == '3':
                    print("Thanks for playing!")
                    break
            print()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    game = In_Between()

    game.game_info()

    while True:
        play = input("""
[1] Play Game
[2] Quit Game

""")
        print()
        if play == '1':
            game.run_game()
        elif play == '2':
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please try again.")
            continue
