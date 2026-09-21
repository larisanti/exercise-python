"""
Curso:
College Algebra with Python (freeCodeCamp)

Objetivo:
Criar equação pra calcular distância entre dois pontos.

Notes:
- ver mais problemas em:
https://cdn.freecodecamp.org/curriculum/college-algebra/AlgebraAndTrigonometry-OP_1tE6R5r.pdf
- frequentes em word/verbal problems:
  - plus, more, increase, up
  - difference, less, decrease, down
  - of, by, factor, area, times
  - out of, per, divided, quotient
"""

import matplotlib.pyplot as plt
import numpy as np

# pontos (tempo em horas, distância em milhas)
x1, y1 = 2/60, 1.4      # 2min = 0.0333h
x2, y2 = 12/60, 0.9     # 12min = 0.2h

# reta y = m·x + b
m = (y2 - y1) / (x2 - x1)
b = y1 - m * x1

print(f"equação: y = {m:.4f}·x + {b:.4f}")

# gráfico
xs = np.linspace(-0.05, 0.35, 200)
ys = m * xs + b

plt.plot(xs, ys, label="y = mx + b")
plt.scatter([x1, x2], [y1, y2], color="red", zorder=5, label="pontos")
plt.xlabel("tempo (h)")
plt.ylabel("distância (mi)")
plt.legend()
plt.grid(True, ls="--", alpha=0.5)
plt.show()
