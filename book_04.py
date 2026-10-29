"""
Referência:
The Recursive Book of Recursion (Al Sweigart) - p. 8

Notes:
- stack = LIFO
- insere = push
- remove = pop
^ insere E remove do topo!
"""

cardStack = []
cardStack.append('5 of diamonds') # 
print(','.join(cardStack))
cardStack.append('3 of clubs')
print(','.join(cardStack))
cardStack.append('ace of hearts')
print(','.join(cardStack))
cardStack.pop() # 
print(','.join(cardStack))