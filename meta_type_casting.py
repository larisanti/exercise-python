"""
Curso:
Programming in Python (Meta - Database Engineer Specialization)

Objetivo: 
Entender como funciona o type casting na conversão implícita e explícita do Python.
"""

# Type casting = data type conversion

# Python entende que int e float são iguais

print(10 == 10)

print(10 == 10.00)

# Python converte automaticamente para float quando soma int com float

print(type(10 + 10.0))

# Tudo que o user digitar é convertido automaticamente para string (class: string)

user_num_1 = input('First number is: ')
user_num_2 = input('Second number is: ')

user_sum = user_num_1 + user_num_2

print(user_sum)

print(type(user_num_1))
print(type(user_num_2))

# Mostrou: class 'str', embora eu tenha digitado números