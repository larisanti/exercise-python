"""
Curso:
Programação III (Uninter - Bacharelado em Engenharia de Software)

Objetivo:
Praticar estrutura de dados.

Notas:
- busca sequencial: olha elemento por elemento, início ao fim
- busca binária: divide o conjunto ao meio, testa o número do meio primeiro
"""

def buscaSequencial(dados, buscado):
    tentativas = 0
    for i in range(len(dados)):
        tentativas += 1
        if dados[i] == buscado:
            print(f"Busca sequencial: encontrou na {tentativas} tentativa")
            return i
    return -1

def buscaBinaria(dados, buscado):
    inicio = 0
    fim = len(dados) - 1
    tentativas = 0

    while inicio <= fim:
        tentativas += 1
        meio = (inicio + fim) // 2

        if dados[meio] == buscado:
            print(f"Busca binária: encontrou na {tentativas} tentativa")
            return meio
        elif buscado > dados[meio]:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1

vetor = [2, 5, 10]
numero_procurado = 2

buscaSequencial(vetor, numero_procurado)
buscaBinaria(vetor, numero_procurado)

