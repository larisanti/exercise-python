"""
Course:
Python (Exercism)

Objective:
Develop functions to classify triangles.

Notes:
- Foi um exercício bem fácil, pois eu já havia feito um semelhante
a diferença é que neste não tem input do usuário.
Achei interessante o teste com pytest substituir o input por lista como argumento.
"""

def equilateral(sides):
    """Returns true if the triangle is equilateral."""
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    return a == b == c

def isosceles(sides):
    """Returns true if the triangle is isosceles."""
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    return a == b or a == c or b == c

def scalene(sides):
    """Returns true if the triangle is scalene."""
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    return a != b and a != c and b != c
