"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo
Praticar resource management.

Notes:
- @contextmanager -> limpeza automática
- usar yield, nunca return
  - yield pausa a função pra usar o recurso
  - return encerra a função e impede o finally de limpar o recurso (vazamento)
"""

@contextmanager
def open_file(file_name, mode):
    try:
        f = open(file_name, mode)
        yield f
    finally:
        file_name.close()
