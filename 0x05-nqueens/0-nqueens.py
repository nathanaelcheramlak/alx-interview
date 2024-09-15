#!/usr/bin/python3
import sys

def print_solutions(solutions):
    """Prints the solutions in the required format"""
    for solution in solutions:
        print(solution)

def is_safe(board, row, col, N):
    """Checks if it's safe to place a queen at board[row][col]"""
    # Check this column in previous rows
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(N):
    """Solves the N Queens problem and prints all solutions"""
    solutions = []
    board = [-1] * N  # This will store the column positions of the queens

    def backtrack(row):
        """Places queens on the board using backtracking"""
        if row == N:
            # A valid solution is found, store the positions
            solution = []
            for r in range(N):
                solution.append([r, board[r]])
            solutions.append(solution)
            return
        
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col  # Place queen
                backtrack(row + 1)  # Try to place the next queen
                board[row] = -1  # Backtrack and remove the queen

    backtrack(0)
    print_solutions(solutions)

if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Check if N is an integer
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N Queens problem
    solve_nqueens(N)
