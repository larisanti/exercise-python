"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo
Praticar collections (containers).

Notes:
- UserString -> classe do módulo collections
^ é um wrapper pra strings
- usado pra criar subclasses de string
- os dados da string ficam no atributo .data
- útil pra personalizar strings sem mudar a original
"""

from collections import UserString
str_name = 'python powered patterned products'
str_word = 'patterned '

# Write your code below!
class SubtractString(UserString):

    def __sub__(self, other):
        if other in self.data:
            self.data = self.data.replace(other, '')

subtract_string = SubtractString(str_name)
subtract_string - str_word
print(subtract_string)