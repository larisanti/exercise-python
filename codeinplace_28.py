"""
Curso:
Code in Place (Stanford)

Objetivo:
Create a while loop in python
"""

def main():
    """
    This function calculates the current value of something that
    repeatedly doubles until it reaches 100 or more.
    """
    curr_value = int(input("Enter a number: "))
    
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value)

if __name__ == '__main__':
    main()
