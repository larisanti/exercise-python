"""
Curso:
Learn Python 3 (Codecademy)

Objetivo:
Criar expressões booleanas (==, !=) para tomar decisões dentro de um bloco if.
"""

# True as the operands are the same 
1 == 1 

# False as the operands are the same 
1 != 1

# True as the operands are different 
2 != 4 

# Evaluates to False as the operands are different
3 == 5     
 
# Evaluates to False as the operands are different types 
"7" == 7   

# Determine if the following boolean expression is True or False
# 2 * 2 == 2 + 2
first_expression = True

# 3 + 3 != 3 * 3 
second_expression = True

# 3 * 3 == '9'
third_expression = False

value = 3*3
print(type(value))


###
x = 20
y = 20

# Create IF statement to check if y and x are esquals
if x == y:
  print("These numbers are the same")


credits = 120

# Write the second if statement here:
if credits >= 120:
  print("You have enough credits to graduate!")

