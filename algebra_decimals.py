"""
Curso:
College Algebra with Python (freeCodeCamp)

Objetivos:
- Introdução à decimais e conversão de frações.

Notes:
- out of = divided
- 1/10 = 0.1 = one tenth
- 1/100 = 0.01 = one hundreth
- 1/1000 = 0.001 = one thousandth
- porcentagem está nos dois primeiros algarismos -> 0.1 = 10%
^ porque porcentagem está nos hundreths
- conversão implícita do python recebe input como str, lembrar
  de formatar (casting) para float/int

Precisei assistir à aula duas vezes e resolver os exercícios no papel.
Preciso de mais tempo para continuar o código, vou dividir em um segundo arquivo.
"""

# expoente positivo
print(10**1)
print(10**2)
print(10**3)

# expoente zero
print(10**0)

# expoente negativo
print(10**-1)
print(10**-2)
print(10**-3)

# sem casting
# text = input("Digite um número: ")
# print(text)

# print(type(text))

# com casting para float
nro = input("Digite um número: ")
print(float(nro))
print(float(nro) + 7)