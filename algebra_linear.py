"""
Curso: 
College Algebra with Python (freeCodeCamp)

Objetivo: 
Encontrar equação completa da reta a partir de dois pontos conhecidos.

Notes:
- slope = M -> how much we move on the graph
- intercept = b -> where we begin in the Y-axis
- fórmula:
  y = M * x + b

Continuo gostando muito do curso e estou fazendo uma aula por semana pra fixar melhor :)
"""

x1 = 1
y1 = 7
x2 = 2
y2 = 10

# slope
m = (y2 - y1) / (x2 - x1)

# intercept (coeficiente linear)
b = y1 - m*x1

# equação completa
print("y = ", m, "x + ", b)
