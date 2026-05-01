"""
Course:
Python (Exercism)

Objective:
Develop functions used in preparing Guido's gorgeous lasagna.

Notes:
Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

# Constants
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2 # I'm defining it to avoid magic numbers.

# Calculate the remaining bake time
def bake_time_remaining(elapsed_bake_time: int):
    """ This function calculates the remaining bake time in minutes. """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

# Calculate the total preparation time
def preparation_time_in_minutes(number_of_layers: int):
    """ 
    To avoid the use of magic numbers, I defined the preparation time as a constant.
    I also added a type hint to the function signature, and
    I considered each layer takes 2 minutes to prepare.
    """
    return number_of_layers * PREPARATION_TIME

# Calculate the total elapsed time
def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int):
    """ This function calculates the total elapsed time in minutes."""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time