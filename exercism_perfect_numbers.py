"""
Course:
Python (Exercism)

Objective:
Praticar matemática.

Notes:
- usar sum() em vez de for -> soma mais rápida
- não precisa criar lista vazia:
  - list comprehension gera os valores e soma diretamente, economiza memória
"""
def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    divisors = [i for i in range(1, number) if number % i == 0]
    aliquot_sum = sum(divisors)

    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    else:
        return "deficient"
