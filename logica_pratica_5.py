"""
Curso:
Lógica de Programação e Algoritmos (Uninter - Bacharelado em Engenharia de Software)

Objetivos:
Praticar operadores condicionais (if/elif/else) e operações lógicas (and/or).
"""

# Classificar triângulos

# O usuário digita os lados do triângulo
A = int(input("Digite o primeiro lado do triângulo: "))
B = int(input("Digite o segundo lado do triângulo: "))
C = int(input("Digite o terceiro lado do triângulo: "))

# Verifica se os valores formam um triângulo: 
# nenhum lado pode ser zero 
# um lado não pode ser maior que a soma dos outros dois
if (A > 0 and B > 0 and C > 0) and (A + B > C and A + C > B and B + C > A):
    
    # Se passou na validação:

    # testa se todos os lados são diferentes (escaleno)
    if A != B and A != C and B != C:
        print("Triângulo escaleno")
    
    # testa se todos os lados são iguais (equilátero)
    elif A == B and B == C:
        print("Triângulo equilátero")
    
    # testa se os dois lados sãoiguais (isósceles)
    else:
        print("Triângulo isósceles")
else:
    # Caso não passe na validação inicial:
    print("O(s) valor(es) digitado(s) não formam um triângulo.")