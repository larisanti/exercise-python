"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo:
Identificar tipos de erros.

Notes:
- sintax errors e exceptions -> duas categorias principais
- traceback -> summary dos erros do tipo exception
- exceptions são objetos da classe Exception que vem de BaseException
- ref: https://docs.python.org/3/library/exceptions.html#BaseException
"""

### Exercício 1

print('Welcome to')
store = 'Instrument World!'
# syntax error
# print(stor))
print(store)


### Exercício 2

sale_instruments = ['Violin', 'Conga', 'Clavinet']

# TypeError: concatenar string + int
# print('The following ' + len('sale_instruments') + ' instruments are on sale:')
print('The following ' + str(len(sale_instruments)) + ' instruments are on sale:')

print(sale_instruments[0])
print(sale_instruments[1])
# IndexError: index fora do tamanho da lista
#print(sale_instruments[3])
print(sale_instruments[2])

# ver de qual classe base o erro deriva
print(TypeError.__bases__)