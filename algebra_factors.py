"""
Curso:
College Algebra with Python (freeCodeCamp)

Objetivo:
- Praticar fatoração.

Notes:
- factoring -> dividing
- factor -> something we multiply
- se o resto <0 então não é fator
- LEMBRAR: módulo (%) retorna o resto
- casting como int
"""

# resto 1
# print(41%10) 

# como reduzri uma fração:
numerator = 12
denominator = 24
factor = 1

# 1. encontrar o maior fator em comum
for test_factor in range(1,denominator+1): 
    if numerator%test_factor==0 and denominator%test_factor==0:
        factor = test_factor 

# 2. dividir pelo maior fator comum encontrado
n = int(numerator/factor) 
d = int(denominator/factor) 

print("original: ", numerator, "/", denominator) 
print("reduced: ", n, "/", d) 
