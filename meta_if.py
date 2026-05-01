"""
Curso:
Programming in Python (Meta - Database Engineer Specialization)

Objetivos: 
Praticar o uso de if/else e de operadores lógicos.
"""

# If + and = as duas condições precisam ser True

a = True
b = True

if a and b:
    print("All true!")

# If + or = uma das condições precisa ser True

a = False
b = True

if not(a) or not(b):
    print("True!")

# Descobrir se o total da bill é maior que 100
bill_total = 114
discount1 = 10

if bill_total > 100:
    print("Bill is greater than 100!")

bill_total = bill_total -discount1

# Descobrir o total da bill
print("Total: " + str(bill_total))

# Descobrir se o total é menor que 100
# Refazer considerando o segundo cenário (< 100)

if bill_total > 100:
    print("Bill is greater than 100!")
    bill_total = bill_total - discount1
    print("Total bill: " + str(bill_total))

else:
    print("Bill is less than 100!")
    print("Total bill: " + str(bill_total))