"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo:
Resolver erro com try/except/else.

Notes: 
- try/except -> try executa, except só executa se ocorrer exception
- try/else -> else só executa se NENHUMA exception ocorrer
- except: trata erro
- else: continua código
- documentação:
  The use of the else clause is better than adding additional code to the try clause because 
  it avoids accidentally catching an exception that wasn't raised by the code being protected by the try...except statement
"""

customer_rewards = {
  'Zoltan': 82570,
  'Guadalupe': 29850,
  'Mario': 17849
}

def display_rewards_account(customer):
  # Write your code below:
  try:
    rewards_number = customer_rewards[customer]
  except KeyError:
    print('Customer was not found in rewards program!')
  else:
    print('Rewards account number is: ' + str(rewards_number))


#customer = 'Zuigly' # keyError, não existe no dict
customer = 'Mario'
display_rewards_account(customer)
