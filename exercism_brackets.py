
"""
Course:
Python (Exercism)

Objective:
Praticar estrutura linear em condicionais.

Notes:
- stack: LIFO (last in, first out) -> último a entrar, primeiro a sair
- Push: Adiciona elementos -> .append(x)
- Pop: Remove elementos -> .pop()
- isEmpty: Verifica se a pilha está vazia -> if not x
- Size: Conta quantos elementos tem na pilha -> len(x)
"""

def is_paired(input_string):
    stack = []
    brackets = {")": "(", "]": "[", "}": "{"}

    for x in input_string:
        if x in "[{(":
            stack.append(x)
        elif x in ")]}":
            if not stack or stack.pop() != brackets[x]:
                return False

    return len(stack) == 0
