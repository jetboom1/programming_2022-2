"""Implemention of the Maze ADT using a 2-D array."""
from arrays import Array2D
from lliststack import Stack


class Maze:
    """Define constants to represent contents of the maze cells."""
    MAZE_WALL = "*"
    PATH_TOKEN = "x"
    TRIED_TOKEN = "o"

    def __init__(self, num_rows, num_cols):
        """Creates a maze object with all cells marked as open."""
        self._maze_cells = Array2D(num_rows, num_cols)
        self._start_cell = None
        self._exit_cell = None

    def num_rows(self):
        """Returns the number of rows in the maze."""
        return self._maze_cells.num_rows()

    def num_cols(self):
        """Returns the number of columns in the maze."""
        return self._maze_cells.num_cols()

    def set_wall(self, row, col):
        """Fills the indicated cell with a "wall" marker."""
        assert 0 <= row < self.num_rows() and \
               0 <= col < self.num_cols(), "Cell index out of range."
        self._maze_cells[row, col] = self.MAZE_WALL

    def set_start(self, row, col):
        """Sets the starting cell position."""
        assert 0 <= row < self.num_rows() and \
               0 <= col < self.num_cols(), "Cell index out of range."
        self._start_cell = _CellPosition(row, col)

    def set_exit(self, row, col):
        """Sets the exit cell position."""
        assert 0 <= row < self.num_rows() and \
               0 <= col < self.num_cols(), "Cell index out of range."
        self._exit_cell = _CellPosition(row, col)

    def find_path(self):
        """
        Attempts to solve the maze by finding a path from the starting cell
        to the exit. Returns True if a path is found and False otherwise.
        """
        stack = Stack()
        blocked_stack = Stack()
        states_stack = Stack()
        stack.push(self._start_cell)
        while not stack.is_empty():
            state = stack.pop()
            states_stack.push(state)
            cell_contains = self._maze_cells[state.row, state.col]
            if self._exit_found(state.row, state.col):
                '''if exit has been found, then backtrack and print the path'''
                while not states_stack.is_empty():
                    state = states_stack.pop()
                    self._mark_path(state.row, state.col)
                while not blocked_stack.is_empty():
                    state = blocked_stack.pop()
                    self._mark_tried(state.row, state.col)
                return True
            elif cell_contains != self.TRIED_TOKEN:
                blocked = True
                self._mark_tried(state.row, state.col)
                if self._valid_move(state.row + 1, state.col):
                    stack.push(_CellPosition(state.row + 1, state.col))
                    blocked = False
                if self._valid_move(state.row - 1, state.col):
                    stack.push(_CellPosition(state.row - 1, state.col))
                    blocked = False
                if self._valid_move(state.row, state.col + 1):
                    stack.push(_CellPosition(state.row, state.col + 1))
                    blocked = False
                if self._valid_move(state.row, state.col - 1):
                    stack.push(_CellPosition(state.row, state.col - 1))
                    blocked = False
                if blocked:
                    blocked_stack.push(state)
        return False

    def reset(self):
        """Resets the maze by removing all "path" and "tried" tokens."""
        pass

    def __str__(self):
        """Returns a text-based representation of the maze."""
        s = ''
        for row in range(self._maze_cells.num_rows()):
            for col in range(self._maze_cells.num_cols()):
                if self._start_cell.row == row and self._start_cell.col == col:
                    s += 'S '
                elif self._exit_cell.row == row and self._exit_cell.col == col:
                    s += 'E '
                elif self._maze_cells[row, col] is None:
                    s += '_ '
                else:
                    s += str(self._maze_cells[row, col]) + ' '
            s += '\n'
        return s

    def _valid_move(self, row, col):
        """Returns True if the given cell position is a valid move."""
        return 0 <= row < self.num_rows() \
               and 0 <= col < self.num_cols() \
               and self._maze_cells[row, col] is None

    def _exit_found(self, row, col):
        """Helper method to determine if the exit was found."""
        return row == self._exit_cell.row and col == self._exit_cell.col

    def _mark_tried(self, row, col):
        """Drops a "tried" token at the given cell."""
        self._maze_cells[row, col] = self.TRIED_TOKEN

    def _mark_path(self, row, col):
        """Drops a "path" token at the given cell."""
        self._maze_cells[row, col] = self.PATH_TOKEN


class _CellPosition(object):
    """Private storage class for holding a cell position."""

    def __init__(self, row, col):
        self.row = row
        self.col = col
