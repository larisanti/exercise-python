"""
Curso:
College Algebra with Python (freeCodeCamp)

Objetivo:
Criar gráfico de funções com numpy. 

Notes:
- numpy calcula todos os valores sem precisar de loop
- sintaxe pra gerar os pontos:
  np.linspace(xmin, xmax, points)
"""

import matplotlib.pyplot as plt
import numpy as np

xmin = -10
xmax = 10
ymin = -10
ymax = 10
points = 2*(xmax-xmin) 
x = np.linspace(xmin, xmax, points)

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'b')
plt.plot([0,0],[ymin,ymax], 'b')

y = 2*x +1
plt.plot(x,y, 'g')

plt.show()