"""
Curso:
College Algebra with Python (freeCodeCamp)

Objetivos:
- Constuir minha própria calculadora como resource para praticar matemática.

Notes:
- Estou construindo durante o curso.
- É super interessante construir uma automatização do que estudei, 
  sinto que o aprendizado se materializa e tem feito sentido (:
- Invés de usar um aplicativo de calculadora, estou usando meus scripts.
- Estou continuando no jupyter notebook: algebra_calculator.ipynb
"""

# Regra de três (proportions)

n1 = 1 # numerador
d1 = 2 # denominador
n2 = 4
d2 = 0 # valor incógnita
answer_variable = "" # valor calculado

# Se n2 for a incógnita
if n2 == 0:
    answer = d2 * n1 / d1
    print("n2 = ", answer)
    n2 = answer 
    answer_variable = "n2"

# Se d2 for a incógnita
if d2 == 0:
    answer = n2 * d1 / n1
    print("d2 = ", answer)
    d2 = answer
    answer_variable = "d2"

# Exibir a proporção completa, não apenas o resultado
if answer_variable:
    print(f"Regra de três: {n1}/{d1} = {n2}/{d2}")
