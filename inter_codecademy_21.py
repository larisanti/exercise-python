"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo:
Compreender função lambda.

Notes:
- Lambda -> uma forma concisa de criar funções de uma única linha
- Variável guardaa função
- Não usar a palavra-chave 'def' nem 'return' (o retorno é implícito)
- Sintaxe: 
   lambda parametro: expressao
- Sintaxe com condicional:
   lambda param: valor_se_true if condicao else valor_se_false
- else é obrigatório quando usar if
"""

def add_bang(sentence):
  print(sentence + '!')

# lambda:
add_bang = lambda string: print(string + '!')
