"""
Curso: 
College Algebra with Python (freeCodeCamp)

Objetivo: 
Resolver um sistema de equação linear com sympy.

Notes:
Achei bem mais rápido resolver com python,
não precisa fazer cálculo de substituição/isolar variável.
Mas a princípio achei mais difícliol ter que transformar em zero
"""

from sympy import *

x,y = symbols('x y')

# igualar equações a zero
e1 = 2*x + y - 1 
e2 = x - 2*y + 7 

# solução
print(linsolve([e1, e2], (x, y))) 
