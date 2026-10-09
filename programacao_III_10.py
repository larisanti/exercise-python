"""
Curso: Programação III (Uninter - Bacharelado em Engenharia de Software)

Tabela Hash - Sistema de emplacamento de veículos

- último número = Estado
- tabela hash -> endereçamento em cadeia
- input deve ser string de 2 letras
- função retorna 7 quando input é DF
- função retorna posição com base no valor ASCII:
  posição = (char1 + char2) % 10
- posicão inicial: None
- input pode ser hard code (via lista, sem solicitar input)
"""

class Nodo:
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None

def funcaoHash(sigla):
    if sigla == "DF":
        return 7
    return (ord(sigla[0]) + ord(sigla[1])) % 10

def inserir(tabela, sigla, nomeEstado):
    posicao = funcaoHash(sigla)
    novo_nodo = Nodo(sigla, nomeEstado)
    novo_nodo.proximo = tabela[posicao]
    tabela[posicao] = novo_nodo

def imprimirTabelaHash(tabela):
    for i in range(10):
        nodo_atual = tabela[i]
        if nodo_atual is None:
            print(f"{i}: None")
        else:
            elementos = []
            while nodo_atual is not None:
                elementos.append(nodo_atual.sigla)
                nodo_atual = nodo_atual.proximo
            elementos.append("None")
            print(f"{i}: {'->'.join(elementos)}")

def main():
    tabelaHash = [None] * 10
    imprimirTabelaHash(tabelaHash)
    print()
    estados = [
        ("AC", "Acre"),
        ("AL", "Alagoas"),
        ("AP", "Amapá"),
        ("AM", "Amazonas"),
        ("BA", "Bahia"),
        ("CE", "Ceará"),
        ("DF", "Distrito Federal"),
        ("ES", "Espírito Santo"),
        ("GO", "Goiás"),
        ("MA", "Maranhão"),
        ("MT", "Mato Grosso"),
        ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"),
        ("PA", "Pará"),
        ("PB", "Paraíba"),
        ("PR", "Paraná"),
        ("PE", "Pernambuco"),
        ("PI", "Piauí"),
        ("RJ", "Rio de Janeiro"),
        ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"),
        ("RO", "Rondônia"),
        ("RR", "Roraima"),
        ("SC", "Santa Catarina"),
        ("SP", "São Paulo"),
        ("SE", "Sergipe"),
        ("TO", "Tocantins")
    ]

    for sigla, nome in estados:
        inserir(tabelaHash, sigla, nome)

    imprimirTabelaHash(tabelaHash)
    print()

    meu_estado = "Larissa de Santi"
    minha_sigla = "LS"
    inserir(tabelaHash, minha_sigla, meu_estado)
    imprimirTabelaHash(tabelaHash)

if __name__ == "__main__":
    main()
