"""
Course:
Python (Exercism)

Objective:
Calculate grains on a chessboard, raising ValueError for invalid squares.

Notes:
- The number of grains on each square is 2^(n-1)
- ValueError = arguments with the wrong value
- Python documentation: https://docs.python.org/3/library/exceptions.html#base-classes
"""

def square(number):
    """Returns the number of grains on a specific square on the chessboard."""
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)

def total():
    """Returns the total number of grains on the chessboard."""
    return 2 ** 64 - 1