"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo
Criar teste unitário.

Notes:
- mais efetivo: gastar tempo escrevendo testes automatizados
- assert -> testa se uma condição é verdadeira
- AssertionError -> se falsa
- usado pra automatizar testes simples
- sintaxe:
  assert condicao, 'mensagem se condicao nao atendida'
"""

destinations = {
  'BUD': 'Budapest',
  'CMN': 'Casablanca',
  'IST': 'Istanbul'
}
print('Welcome to Small World Airlines!')
print('What is the airport code of your travel destination?')
destination = 'HND'


# Write your code below: 
assert destination in destinations, 'Sorry, Small World currently does not fly to this destination!'
city_name = destinations[destination]
print('Great! Retrieving information for your flight to ...' + city_name)
