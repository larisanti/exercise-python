"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo
Praticar resource management.

Notes:
- with é usado pra gerenciar resources
- sem with -> usar try/finally
- vazamento de memória -> quando o programa mantém recursos/processos sem necessidade
"""

try:
  open_file = open('file_name.txt', 'r')
  print(open_file.read())
finally:
  open_file.close()

with open('file_name.txt', 'r') as open_file:
  print(open_file.read())
  
