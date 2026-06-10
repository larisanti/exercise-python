"""
Course:
Python (Exercism)

Objective:
Praticar operações com números inteiros.

Notes:
- Verificar se é par: numero % 2 == 0
- Inserir ValueError no início pra evitar bugs
"""
def steps(number):
    # 1. Validar
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    
    # 2. Contar etapas
    step_count = 0
    
    # 3. Loop até chegar a 1
    while number > 1:
        if number % 2 == 0:
            number = number // 2  # se par: // 2
        else:
            number = number * 3 + 1  # se ímpar: * 3 + 1
            
        step_count += 1 # incrementar o contador

    return step_count