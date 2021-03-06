"""This module contains Board and Game classes."""
import random
from copy import deepcopy
from btree import Tree


class Board:
    """ This class defines a game board."""
    def __init__(self, data=None, last_move="0"):
        """
        list, str -> ()
        Initializes a board object.
        """
        if data is None:
            self.data = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        else:
            self.data = deepcopy(data)
        self.last_move = last_move
        self.win = self.check_win()

    def person_move(self):
        """
        self -> ()
        Moves as a person.
        """
        possible_moves = self.free_cells()
        if not possible_moves:
            pass
        move = random.choice(possible_moves)
        self.data[int(move[0])][int(move[1])] = 'x'
        self.last_move = 'x'

    def free_cells(self):
        """
        self -> list
        Forms a list of free cells.
        """
        free_cells = []
        for i, element1 in enumerate(self.data):
            for j, element in enumerate(element1):
                if element == ' ':
                    free_cells.append((i, j))
        return free_cells

    def check_win(self):
        """
        self -> bool
        Checks for the winning position.
        """
        for lst in self.data:
            if lst[0] == lst[1] == lst[2] and lst[0] != ' ':
                return True
        for j in range(3):
            if self.data[0][j] == self.data[1][j] == self.data[2][j] and self.data[1][j] != ' ':
                return True
        if self.data[0][0] == self.data[1][1] == self.data[2][2] and self.data[1][1] != ' ':
            return True
        if self.data[0][2] == self.data[1][1] == self.data[2][0] and self.data[1][1] != ' ':
            return True
        return False

    def computer_move(self):
        """
        self -> ()
        Moves as a computer.
        """
        best_option = self.find_next_board(self.tree_creation())

        self.data = best_option.data
        self.last_move = '0'

    def tree_creation(self):
        """
        self -> tree
        Creates a game boards tree.
        """
        tree = Tree(self)

        def recursion(tree):
            free_cells = tree.root.free_cells()
            if not free_cells or tree.root.check_win():
                return
            if len(free_cells) == 1:
                board = deepcopy(tree.root)
                board.last_move = board.get_player(board.last_move)
                board.data[free_cells[0][0]][free_cells[0][1]] = board.last_move
                tree.right = Tree(board)
                recursion(tree.right)
                return
            board1 = deepcopy(tree.root)
            board1.last_move = board1.get_player(board1.last_move)
            position = random.choice(free_cells)
            free_cells.remove(position)
            board1.data[position[0]][position[1]] = board1.last_move
            tree.right = Tree(board1)

            board2 = deepcopy(tree.root)
            board2.last_move = board2.get_player(board2.last_move)
            position = random.choice(free_cells)
            free_cells.remove(position)
            board2.data[position[0]][position[1]] = board2.last_move
            tree.left = Tree(board2)
            recursion(tree.right)
            recursion(tree.left)

        recursion(tree)
        return tree

    def find_next_board(self, tree_):
        """
        self, tree -> board
        Finds the optimal board for the next move.
        """
        option1 = tree_.left
        option2 = tree_.right

        def find_recursively(tree):
            if not tree or tree.root.free_cells():
                return 0
            if tree.last_move == '0' and tree.root.check_win():
                return 1
            return 0 + find_recursively(tree.right) + find_recursively(tree.left)

        sum_option1 = find_recursively(option1)
        sum_option2 = find_recursively(option2)
        if sum_option1 > sum_option2:
            return option1.root
        return option2.root

    def __str__(self):
        """
        self -> str
        Forms a string representation of the board.
        """
        string = ''
        for element in self.data:
            string += str(element) + '\n'
        return string

    @staticmethod
    def get_player(last_player):
        """
        self -> ()
        Gets the current player.
        """
        if last_player == 'x':
            return '0'
        return 'x'


class Game:
    """ This class defines a game."""
    def __init__(self, board):
        """
        board -> ()
        Initializes a game object.
        """
        self.board = board

    def game_state(self):
        """
        self -> ()
        Prints the current state of the board.
        """
        for i in self.board.data:
            print(i)

    def play(self):
        """
        self -> ()
        Plays the game.
        """
        while True:
            self.board.person_move()
            print(self.board)
            if self.board.check_win() or not self.board.free_cells():
                break
            self.board.computer_move()
            print(self.board)
            if self.board.check_win() or not self.board.free_cells():
                break

        print('The game is over!')
