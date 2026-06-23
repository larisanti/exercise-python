"""
Curso:
College Algebra with Python (freeCodeCamp)

Objetivos:
- Praticar notação de funções.
- Compreender a lógica de input/output em funções.

Notes:
- função consiste em:
    1. receber um input, 
    2. realizar uma operação com ela,
    3. gerar um output
"""

# f(x) = x + 2 em python é:

def f(x):
    return x + 2

print(f(3))

# automatizar a função com loop
def f(x):
    y = 10 * x + 5
    return y 

for x in range(5):
    resultado = f(x)
    print(x, "\t", resultado)
