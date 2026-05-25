"""
Course:
Python (Exercism)

Objective:
Practice loops and bolean logic.
"""

def leap_year(year):
    """
    Function used to determine if a year is a leap year.
    """

    # divisible by 400 = leap year
    if year % 400 == 0:
        return True
    # divisible by 100 = not leap year
    elif year % 100 == 0:
        return False
    # divisible by 4 = leap year
    elif year % 4 == 0:
        return True
    # not divisible by 4 = not leap year
    else:
        return False