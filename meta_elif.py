"""
Curso:
Programming in Python (Meta - Database Engineer Specialization)

Objetivo: 
Introdução ao uso de elif em condicionais.
"""

# elif: como se fosse mais um if,  mas só é testado se o if anterior for falso

# Considerar 2 condições para ter desconto:
# 1. Ser loyal customer
# 2. Spent > 100

loyalty_customer = True
total_bill = 124

if loyalty_customer and total_bill > 100:
    # Desconto de 20%
    total_bill = total_bill - (float(total_bill)/ 100) * 20
elif total_bill > 100:
    # Desconto de 10%
    total_bill = total_bill - (float(total_bill)/ 100) * 10
else:
    # Sem desconto: aplica taxa de 5%
    print('Sorry, no discount. 5% service charge applied.')
    total_bill = total_bill + (float(total_bill) / 100) * 5


print('Total: ', float(total_bill))
