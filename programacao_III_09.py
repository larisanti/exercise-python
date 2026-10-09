"""
Curso: Programação III (Uninter - Bacharelado em Engenharia de Software)

Lista Encadeada - Classificar ordem de atendimento

A = maior urgência / V = menor urgência
- entre A -> numeração menor primeiro (a partir do 201)
- entre V -> numeração menor primeiro (a partir do 1)
- lista não circular -> ultimo nodo proximo = None
- nodo = cartão
- head = início da fila
"""

class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None

class FilaAtendimento:
    def __init__(self):
        self.head = None
    
    def inserirSemPrioridade(self, nodo):
        if self.head is None:
            self.head = nodo
            return
    
        paciente = self.head
        while paciente.proximo != None:
            paciente = paciente.proximo
    
        paciente.proximo = nodo

# fila = FilaAtendimento()
# p1 = Nodo(1, 'V')
# p2 = Nodo(201, 'A')
# fila.inserirSemPrioridade(p1)
# fila.inserirSemPrioridade(p2)
# print(fila.head.numero, fila.head.cor)
# print(fila.head.proximo.numero, fila.head.proximo.cor)

    def inserirComPrioridade(self, nodo):
        if self.head is None:
            self.head = nodo
            return

        if self.head.cor == "V":
            nodo.proximo = self.head
            self.head = nodo
            return

        nodo_atual = self.head
        while nodo_atual.proximo is not None and nodo_atual.proximo.cor == "A":
            nodo_atual = nodo_atual.proximo

        nodo.proximo = nodo_atual.proximo
        nodo_atual.proximo = nodo

# fila = FilaAtendimento()
# fila.inserirSemPrioridade(Nodo(2, "V"))
# fila.inserirComPrioridade(Nodo(202, "A"))
# print("1o da fila:", fila.head.numero, fila.head.cor)
# print("2o da fila:", fila.head.proximo.numero, fila.head.proximo.cor)

contador_v = 1
contador_a = 201
fila = FilaAtendimento()

def inserir():
    global contador_v, contador_a

    cor = input("Informe a cor do cartão (A/V): ").strip().upper()
    while cor not in ["A", "V"]:
        print("Cor inválida! Digite A ou V.")
        cor = input("Informe a cor do cartão (A/V): ").strip().upper()

    if cor == "V":
        numero = contador_v
        contador_v += 1
    else:
        numero = contador_a
        contador_a += 1

    print(f"Informe o número do cartão: {numero}")

    nodo = Nodo(numero, cor)

    if fila.head is None:
        fila.head = nodo
    elif cor == "V":
        fila.inserirSemPrioridade(nodo)
    elif cor == "A":
        fila.inserirComPrioridade(nodo)

def imprimirListaEspera():
    nodo_atual = fila.head
    elementos = []
    while nodo_atual is not None:
        elementos.append(f"[{nodo_atual.cor},{nodo_atual.numero}]")
        nodo_atual = nodo_atual.proximo

    print("Lista -> " + " ".join(elementos))

def atenderPaciente():
    if fila.head is None:
        print("Fila vazia! Nenhum paciente para atender.")
        return

    paciente = fila.head
    fila.head = fila.head.proximo
    print(f"Atendendo o paciente cartão cor {paciente.cor} e número {paciente.numero}")

# Menu e testes
def main():
    while True:
        print("1 - Adicionar paciente a fila")
        print("2 - Mostrar pacientes na fila")
        print("3 - Chamar paciente")
        print("4 - sair")

        opcao = input("")

        if opcao == "1":
            inserir()
        elif opcao == "2":
            imprimirListaEspera()
        elif opcao == "3":
            atenderPaciente()
        elif opcao == "4":
            print("Encerrando...")
            break
        else:
            print("Selecione outra opção!\n")

if __name__ == "__main__":
    main()