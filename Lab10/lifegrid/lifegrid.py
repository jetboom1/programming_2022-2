from arrays import Array2D


class LifeGrid:
    """
    Implements the LifeGrid ADT for use with the Game of Life.
    """
    # Defines constants to represent the cell states.
    DEAD_CELL = 0
    LIVE_CELL = 1

    def __init__(self, num_rows, num_cols):
        """
        Creates the game grid and initializes the cells to dead.
        :param num_rows: the number of rows.
        :param num_cols: the number of columns.
        """
        # Allocates the 2D array for the grid.
        self._grid = Array2D(num_rows, num_cols)
        # Clears the grid and set all cells to dead.
        self.configure(list())

    def num_rows(self):
        """
        Returns the number of rows in the grid.
        :return: the number rows in the grid.
        """
        return self._grid.num_rows()

    def num_cols(self):
        """
        Returns the number of columns in the grid.
        :return:Returns the number of columns in the grid.
        """
        return self._grid.num_cols()

    def configure(self, coord_list):
        """
        Configures the grid to contain the given live cells.

        :param coord_list: [(1, 1), (1, 2), (2, 2), (3, 2)]
        :return:
        """
        for (row, col) in coord_list:
            self._grid.__setitem__((row,col), self.LIVE_CELL)
        return True

    def is_live_cell(self, row, col):
        """
        Does the indicated cell contain a live organism?

        :param row: row of the cell.
        :param col: column of the cell.
        :return: the result of check.
        """
        if self._grid.__getitem__((row, col)) == self.LIVE_CELL:
            return True
        return False

    def clear_cell(self, row, col):
        """
        Clears the indicated cell by setting it to dead.
        :param row: row of the cell.
        :param col: column of the cell.
        """
        self._grid[row][col] = self.DEAD_CELL

    def set_cell(self, row, col):
        """
        Sets the indicated cell to be alive.
        :param row: row of the cell.
        :param col: column of the cell.
        """
        self._grid[row][col] = self.LIVE_CELL

    def num_live_neighbors(self, row, col):
        """
        Returns the number of live neighbors for the given cell.
        :param row: row of the cell.
        :param col: column of the cell.
        :return:
        """
        neighbors = [(row - 1, col), (row + 1, col),
                     (row, col - 1), (row, col + 1)]
        count = 0
        for (r, c) in neighbors:
            if not (0 <= r < self.num_rows() and 0 <= c < self.num_cols()):
                continue
            if self.is_live_cell(r, c):
                count += 1
        return count
    def __str__(self):
        """
        Returns string representation of LifeGrid
        in form of:
        DDLDD
        DLDLD
        DLDLD
        DDLDD
        DDDDD
        Where D - dead cell, L - live cell
        """
        s = ""
        for row in range(self.num_rows()):
            for col in range(self.num_cols()):
                if self.is_live_cell(row, col):
                    s += "L"
                else:
                    s += "D"
            s += "\n"
        return s
