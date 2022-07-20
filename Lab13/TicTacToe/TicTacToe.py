import copy

from linked_binary_tree import LinkedBinaryTree


class CellIsOccupied(Exception):
    pass


class InvalidMove(Exception):
    pass


class Board:
    """board class for representing a current state of the game"""

    def __init__(self):
        self.board = [[' '] * 3 for i in range(3)]
        self.last_move_player = None
        self.last_move_coords = (None, None)

    def get_status(self):
        """checks the status of the game: if someone won or not. Returns 'x' or 'o' or 'draw' or 'continue'"""
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    return 'continue'
        return 'draw'

    def make_move(self, pos: tuple, turn: str):
        '''makes move. position is a tuple of coordinates of the cell. turn is a player`s symbol'''
        try:
            if self.board[pos[0]][pos[1]] != ' ':
                raise CellIsOccupied
            self.board[pos[0]][pos[1]] = turn
            self.last_move_player = turn
            self.last_move_coords = pos
        except IndexError:
            raise InvalidMove

    def build_tree(self):
        '''build a binary tree, representing possible outcomes of the game'''
        tree = LinkedBinaryTree(self)

        def recurse_tree(board, tree):
            chips = ['x', 'o']
            if board.get_status() == 'continue':
                moves = 0
                for i in range(3):
                    for j in range(3):
                        if board.board[i][j] == ' ':
                            if moves == 0:
                                left_variant = copy.deepcopy(board)
                                left_variant.make_move((i, j), chips[chips.index(board.last_move_player) - 1])
                                tree.insert_left(left_variant)
                            elif moves == 1:
                                right_variant = copy.deepcopy(board)
                                right_variant.make_move((i, j), chips[chips.index(board.last_move_player) - 1])
                                tree.insert_right(right_variant)
                            moves += 1
                        if moves == 2:
                            recurse_tree(left_variant, tree.left_child)
                            recurse_tree(right_variant, tree.right_child)
                            break
            return tree

        return recurse_tree(self, tree)

    def calculate_scores(self, tree):
        '''calculates scores of the tree. Returns tuple (left_score, right_score)'''

        def recurse(tree):
            if tree.left_child is None and tree.right_child is None:
                if tree.key.get_status() == 'o':
                    return 1
                elif tree.key.get_status() == 'x':
                    return -1
                else:
                    return 0
            else:
                try:
                    return recurse(tree.left_child) + recurse(tree.right_child)
                except AttributeError:
                    if tree.left_child is None:
                        return recurse(tree.right_child)
                    elif tree.right_child is None:
                        return recurse(tree.left_child)

        try:
            score_left, score_right = recurse(tree.left_child), recurse(tree.right_child)
        except AttributeError:
            if tree.left_child is None and tree.right_child is not None:
                score_right = recurse(tree.right_child)
                score_left = -10
            elif tree.right_child is None and tree.left_child is not None:
                score_left = recurse(tree.left_child)
                score_right = -10
            else:
                score_left = score_right = 0
        return score_left, score_right

    def decide_best_move(self):
        '''decides the best move at the current state of the game. Returns tuple (x, y) with the coordinates
        of the next move'''
        decision_tree = self.build_tree()
        score_left, score_right = self.calculate_scores(decision_tree)
        if score_left > score_right:
            return decision_tree.left_child.key.last_move_coords
        else:  # if scores are equal we can choose any move
            try:
                return decision_tree.right_child.key.last_move_coords
            except AttributeError:
                raise InvalidMove

    def make_computer_move(self):
        '''makes computer move'''
        best_move = self.decide_best_move()
        self.make_move(best_move, 'o')

    def __str__(self):
        '''returns a string representation of the board'''
        return '\n'.join([''.join(str(row)) for row in self.board])

    def game(self):
        '''The interface of the game'''
        print('Welcome to our game!')
        while True:
            print(self)
            if self.get_status() == 'continue':
                player_move = map(int, input('Enter your move (e.g "0 1" - first row second column):').split(' '))
                try:
                    self.make_move(tuple(player_move), 'x')
                except CellIsOccupied:
                    print('Error: This cell is already occupied')
                    continue
                except InvalidMove:
                    print('Error: Invalid coordinates')
                    continue
                try:
                    self.make_computer_move()
                except InvalidMove: #it means draw
                    continue
            elif self.get_status() == 'draw':
                print('Draw!')
                break
            elif self.get_status() == 'x':
                print('You won!')
                break
            elif self.get_status() == 'o':
                print('Sorry, computer bet you. Good luck next time :)')
                break


if __name__ == '__main__':
    board = Board()
    board.game()
