"""
Referência:
Python Programming Exercises, Gently Explained (Al Sweigart) - p. 23
"""

def printASCIITable():
    for i in range(32, 127):
        print(i, chr(i))

printASCIITable()
    
#print(ord('L'))
#print(chr(76))