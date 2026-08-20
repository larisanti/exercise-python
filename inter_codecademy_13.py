"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo:
Praticar namespace do tipo local.

Notes:
- criado quando uma função é executada e destruído quando ela termina.
- guarda parâmetros da função e variáveis criadas dentro dela.
- locals() dentro de uma função retorna seu namespace local.
- locals() fora de qualquer função se comporta igual a globals().
- regra de ordem de busca de variáveis (LEGB):
  L = Local (dentro da função atual)
  E = Enclosing (função envolvente / escopo aninhado)
  G = Global (nível do arquivo/módulo)
  B = Built-in (recursos nativos do Python)
"""
global_variable = 'global'

print(' -- Local and global Namespaces with empty script -- \n')
# Write Checkpoint 1 here:
print(locals())
print(globals())

# Write Checkpoint 2 here:
def divide(num1, num2):
  result = num1 / num2
  print(locals()) 

# Write Checkpoint 3 here:
def multiply(num1, num2):
  product = num1 * num2
  print(locals())

print(' \n -- Local Namespace for divide -- \n')
# Write Checkpoint 4 here:
divide(3, 4)

print(' \n -- Local Namespace for multiply -- \n')
# Write Checkpoint 5 here:
multiply(4, 50)

print(' \n -- Local Namespace final -- \n')
# Write Checkpoint 6 here:
print(locals())