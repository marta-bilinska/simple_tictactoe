import random
from copy import deepcopy


class Board:
    def __init__(self, data=None, last_move="0"):
        if data is None:
            self.data = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        else:
            self.data = deepcopy(data)
        self.last_move = last_move
        self.win = self.check_win()

    def person_move(self):
        possible_moves = self.free_cells()
        if not possible_moves:
            pass
        move = random.choice(possible_moves)
        self.data[int(move[0])][int(move[1])] = 'x'
        self.last_move = 'x'

    def free_cells(self):
        free_cells = []
        for i, el in enumerate(self.data):
            for j, element in enumerate(el):
                if element == ' ':
                    free_cells.append((i, j))
        return free_cells

    def check_win(self):
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
        best_option = self.find_next_board(self.tree_creation())

        self.data = best_option.data
        self.last_move = '0'

    def tree_creation(self):
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
        s = ''
        for el in self.data:
            s += str(el) + '\n'
        return s

    @staticmethod
    def get_player(last_player):
        if last_player == 'x':
            return '0'
        return 'x'


class Game:
    def __init__(self, board):
        self.board = board

    def game_state(self):
        for i in self.board.data:
            print(i)

    def play(self):
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
