"""
Curso:
College Algebra with Python (freeCodeCamp)

Objetivo:
Plotar gráficos de funções com matplotlib e numpy. 

Notes:
- graphing system = plotar equações
- fluxo:
  1. import
  2. definir parâmetros/limites
  3. criar eixo x
  4. calcular equações
  5. plotar

"""

import matplotlib.pyplot as plt
import numpy as np

xmin = -10
xmax = 10
ymin = -10
ymax = 10

# quantidade de pontos pra suavizar curvas
points = 10*(xmax-xmin)

# definir x
x = np.linspace(xmin,xmax,points)

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'b')
plt.plot([0,0],[ymin,ymax], 'b')

# linha 1
y1 = 2*x
plt.plot(x, y1) 

# linha 2
y2 = x**2
plt.plot(x, y2) 

ax.grid(True)
plt.show()