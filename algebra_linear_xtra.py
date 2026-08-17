"""
Curso: 
College Algebra with Python (freeCodeCamp)

Objetivo: 
Encontrar equação completa da reta a partir de dois pontos conhecidos.

Notes:
- eixo X -> independent variable (tempo, causa)
- eixo Y -> dependent variable (lucro, população)
- intercept é o valor inicial quando x = 0
- ordem:
  plt.axis([xmin, xmax, ymin, ymax])
"""

import matplotlib.pyplot as plt

x1 = 0
y1 = 0
x2 = 40
y2 = 13

# y = mx + b
m = (y2 - y1) / (x2 - x1)
b = y1 - m*x1
print("y = ", m, "x + ", b)

# variáveis da window
xmin = 0
xmax = 100
ymin = 0
ymax = 50

# linhas
y3 = m*xmin + b 
y4 = m*xmax + b 

# setup
fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'b')
plt.plot([0,0],[ymin,ymax], 'b')

# labels de x e y
ax.set_xlabel("thousands")
ax.set_ylabel("tons")
ax.grid(True)

# sintaxe da cor da linha
plt.plot([xmin,xmax],[y3,y4],'b')

plt.show()