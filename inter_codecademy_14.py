"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo:
Praticar namespace do tipo enclosing.

Notes:
- criado em funções aninhadas (nested functions)
- a função externa é a "enclosing function" e a interna é a "enclosed function"
- a função interna tem acesso às variáveis do namespace da função externa
"""

global_variable = 'global'
 
def outer_function():
  outer_value = "outer"
 
  def inner_function():
    inner_value = "inner"

    def inner_nested_function():
      nested_value = 'nested'
    inner_nested_function()
    # Add locals() below
    print(locals())
  inner_function()
 
outer_function()