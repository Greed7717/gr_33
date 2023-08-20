
# pip install python-decouple
# pip freeze > requirements.txt

import random

class CasinoGame:
    def __init__(self, initial_money):
        self.money = initial_money
        self.slots = list(range(1, 31))

    def make_bet(self, slot, amount):
        winning_slot = random.choice(self.slots)
        if slot == winning_slot:
            self.money += amount * 2
            return True
        else:
            self.money -= amount
            return False

class GameLogic:
    @staticmethod
    def determine_result(player_won):
        if player_won:
            return "Congratulations! You won!"
        else:
            return "Sorry, you lost."

MY_MONEY=1000

from decouple import config
from casino_game import CasinoGame
from game_logic import GameLogic


def main():
    initial_money = int(config('MY_MONEY'))
    game = CasinoGame(initial_money)
    logic = GameLogic()

    while True:
        print(f"Your current money: ${game.money}")
        slot = int(input("Choose a slot (1-30): "))
        bet = int(input("Place your bet: "))

        if bet > game.money:
            print("Not enough money!")
            continue

        player_won = game.make_bet(slot, bet)
        result_message = logic.determine_result(player_won)
        print(result_message)

        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            print(f"Final money: ${game.money}")
            break


if __name__ == "__main__":
    main()
