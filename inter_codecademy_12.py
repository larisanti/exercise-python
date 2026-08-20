"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo:
Praticar namespace do tipo global.

Notes:
- inicia quando o arquivo principal é executado e 
dura até terminar de rodar o programa
- guarda apenas elementos do nível principal do arquivo
^ ignora funções
- módulos importados ficam isolados em seu próprio namespace
^ por isso acesso o conteúdo usando "." -> ramdom.randit
- ordem de busca de variáveis: LEGB
"""

# ver todos os objetos que estão em variáveis globais
# print(globals())

print(' -- Globals Namespace with empty script -- \n')
print(globals())

global_variable = 'global'

def print_global():
  global_variable = 'nested global'
  nested_variable = 'nested value'

print(' \n -- Globals Namespace non-empty script -- \n')
print(globals())