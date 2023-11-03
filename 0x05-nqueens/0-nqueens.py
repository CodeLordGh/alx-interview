#!/usr/bin/python3

import sys

class Queen:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def is_attacking(self, other):
        """Returns True if this queen is attacking the other queen, False otherwise."""
        return self.row == other.row or self.col == other.col or abs(self.row - other.row) == abs(self.col - other.col)

class NQueensSolver:
    def __init__(self, n):
        self.n = n
        self.board = [[None for i in range(n)] for j in range(n)]
        self.solutions = []

    def solve(self):
        """Solves the N queens problem and returns a list of all solutions."""
        self.place_queen(0)
        return self.solutions

    def place_queen(self, col):
        """Attempts to place a queen in the given column. If successful, recursively places the next queen in the next column. If unsuccessful, backtracks."""
        if col == self.n:
            # All queens have been placed successfully.
            self.solutions.append([Queen(row, col) for row in range(self.n)])
            return

        for row in range(self.n):
            if self.is_safe_to_place_queen(row, col):
                # Place the queen in the given row and column.
                self.board[row][col] = Queen(row, col)

                # Recursively place the next queen in the next column.
                self.place_queen(col + 1)

                # Backtrack if no solution was found in the next column.
                if not self.solutions:
                    self.board[row][col] = None

    def is_safe_to_place_queen(self, row, col):
        """Returns True if it is safe to place a queen in the given row and column, False otherwise."""
        for other in self.board:
            if other is not None and other.is_attacking(Queen(row, col)):
                return False

        return True

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solver = NQueensSolver(n)
    solutions = solver.solve()

    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()

