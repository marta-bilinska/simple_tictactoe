"""
This module contains a main function of a program.
"""
from board import Game, Board


def main():
    """This function start and plays the game."""
    print("Starting the game.")
    initial_board = Board()
    game = Game(initial_board)

    game.play()


if __name__ == "__main__":
    main()
