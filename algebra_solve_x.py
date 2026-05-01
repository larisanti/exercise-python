"""
Curso: 
College Algebra with Python (freeCodeCamp)

Objetivo: 
Utilizar Python para resolver equações do primeiro grau com uma variável.

Notes:
- Com sympy é possível criar variáveis sem um valor númerico
- Python não tem built in function para reconhecer X como símbolo matemático
- Não precisa de print quando usar solve em um notebook
- Usar iteração para percorrer uma lista de soluções (quando não sei quantas)
"""

# Solving for X

import sympy
from sympy import symbols
from sympy.solvers import solve

# Definir a variável com sympy
x = symbols('x')

# Para resolver da forma mais simples
eq = 3*x - 6

# ou: solve(eq,x)
print("x = ", solve(eq,x))

# Para criar a equação no terminal
eq = input('Enter equation: 0 = ')
print("x = ", solve(eq,x))

# Para armazenar o resultado
eq = 2*x - 4

solution = solve(eq,x)
print("x = ", solution[0])

# Para multiple answers ou quando não sei quantas
eq = input('Enter equation: 0 = ')

solution = solve(eq,x)

# Usar iteração pra percorrer a lista
for s in solution:
    print("x = ", s)