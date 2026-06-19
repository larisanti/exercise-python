"""
Curso:
Code in Place (Stanford)

Objetivo:
Create an if/else statement in python
"""

#  Assume for now that the minimum height is 50 of whatever height unit you'd like :)
MINIMUM_HEIGHT = 50

def main():
    user_input = input("How tall are you? ")
    height = float(user_input)
    
    if height >= MINIMUM_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")

if __name__ == '__main__':
    main()