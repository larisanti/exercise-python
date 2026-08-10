"""
Course:
Python (Exercism)

Objectives:
Praticar tratamento de strings e comparadores.

Notes:
- usar enumerated constants 
^ atribuir int porque é mais eficiente na memória
- transformar em string e comparar
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    
    if not list_one:
        return SUBLIST
    
    if not list_two:
        return SUPERLIST
    
    s1 = str(list_one)[1:-1]+","
    s2 = str(list_two)[1:-1]+","
    
    if s1 in s2:
        return SUBLIST
    
    if s2 in s1:
        return SUPERLIST
    
    return UNEQUAL