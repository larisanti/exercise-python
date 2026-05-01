"""
Course:
Python (Exercism)

Objective:
Develop functions for tracking poker hands and assorted card tasks.

Notes: 
- Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
- I finally understood that iteration (iteração) in lists means going through the list one item at a time.
- When I use for loops, while loops, and "in", I'm iterating (iterando) through the list.
- in = operator (operador)
- index = position
"""

# 1. Tracking Poker Rounds
def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    return [number, number + 1, number + 2]


# 2. Keeping all Rounds in the Same Place
def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


# 3. Finding Prior Rounds
def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    return number in rounds


# 4. Averaging Card Values
def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    return sum(hand) / len(hand)


# 5. Alternate Averages
def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    # Primeira condição checa a média das pontas (first e last values)
    condicao_1 = card_average(hand) == (hand[0] + hand[-1]) / 2
    # Segunda condição checa a carta do meio e se ela é igual a média
    condicao_2 = card_average(hand) == hand[len(hand) // 2]

    return condicao_1 or condicao_2


# 6. More Averaging Techniques
def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    
    # odd: [1::2] / even: [0::2]
    return card_average(hand[1::2]) == card_average(hand[0::2])


# 7. Bonus Round Rules
def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        hand[-1] = hand[-1] * 2

    return hand
