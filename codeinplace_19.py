"""
Curso:
Code in Place (Stanford)

Objetivos:
- Revisar strings, f-strings e input.

Notes:
- Em f-string -> executa primeiro o lado direito
"""

def main():
    name = input("What is your name? ")
    print(f"{name}")
    print(f"{name}!")
    print(f"{name}✨")

if __name__ == '__main__':
    main()