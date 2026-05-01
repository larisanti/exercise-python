"""
Curso:
Lógica de Programação e Algoritmos (Uninter - Bacharelado em Engenharia de Software)

Objetivos:
Praticar o fatiamento de strings.
"""

# Peça uma frase ao usuário, armazene apenas a sua primeira metade em uma nova variável e exiba os dois últimos caracteres dessa metade.
frase_usuario = input("Digite uma frase qualquer: ")

# Fatiar a string para obter a primeira metade
meio = len(frase_usuario) // 2
primeira_metade = frase_usuario[:meio]

print(f"A primeira metade é: {primeira_metade}")
print(f"Os dois últimos caracteres da metate são: {primeira_metade[-2:]}")
