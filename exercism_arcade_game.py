"""
Course:
Python (Exercism)

Objective:
Develop functions for implementing the rules of the classic arcade game Pac-Man.
"""


def eat_ghost(power_pellet_active, touching_ghost):
    """Function to verify if Pac-Man can eat a ghost 
    Conditions (both):
    - Is empowered by a power pellet?
    - Is touching a ghost?
    """
    return power_pellet_active and touching_ghost


def score(touching_power_pellet, touching_dot):
    """Function to verify if Pac-Man has scored
    Conditions (one or another):
    - Is touching a power pellet?
    - Is touching a dot?
    """
    return touching_power_pellet or touching_dot


def lose(power_pellet_active, touching_ghost):
    """ Function to verify if Pac-Man has lost
    Conditions (one and other):
    - Is empowered by a power pellet? (not)
    - Is touching a ghost? (and)
    """
    return not power_pellet_active and touching_ghost


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Function to verify if Pac-Man has won
    Conditions (ordem: not, and, or):
    - Has eaten all the dots? (must be true)
    - Is empowered by a power pellet? (or if touching ghost)
    - Is touching a ghost? (not)
    """
    return has_eaten_all_dots and (not touching_ghost or power_pellet_active)