"""
Curso:
Code in Place (Stanford)

Objetivos:
- Revisar variáveis e operações.

Notes:
- A variable is a place to store information in a program
^ como x em algebra ser uma box que contém um número
- Variable -> name + value associado ao name 
- sinal = significa assignment e não igualdade
- Nome passa ser um objeto depois de ter um valor associado
- Objeto pode ter diferentes tamanhos, ocupar mais ou menos espaço na RAM
- real value = float
"""

# This program calculate the ages of Anton, Beth, Chen, Drew and Ethan
def main():
    anton = 21
    beth = 6 + anton
    chen = 20 + beth
    drew = chen + anton
    ethan = chen

    print("Anton is " + str(anton))
    print("Beth is " + str(beth))
    print("Chen is " + str(chen))
    print("Drew is " + str(drew))
    print("Ethan is " + str(ethan))

if __name__ == '__main__':
    main()

