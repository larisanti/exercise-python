"""
Curso:
College Algebra with Python (freeCodeCamp)

Objetivo:
Criar gráfico de funções com matplotlib. 

Notes:
- ro = red circle
- as funciona como um alias, posso escolher outro
- melhor prática: .show() no final
- achei o conteúdo de matemática fácil, mas foi importante revisar
pois o professor sempre menciona dicas de boas práticas.
"""

import matplotlib.pyplot as plt

xmin = -15
xmax = 15
ymin = -15
ymax = 15

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'b')
plt.plot([0,0],[ymin,ymax], 'g')

for x in range(xmin, xmax):
    y = 0.5*x + 1
    plt.plot([x],[y], 'ro')

plt.show()
