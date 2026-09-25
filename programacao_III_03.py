"""
Curso:
Programação III (Uninter - Bacharelado em Engenharia de Software)

Objetivo:
Praticar recursão

Notas:
- fibonacci = função recursiva que chama ela 2x
              ^ cada número é a soma dos dois anteriores:
           fib(5)
          /      \
       fib(4)   fib(3)
       /   \     /   \
    fib(3) fib(2) fib(2) fib(1)
    /   \
 fib(2) fib(1)

"""

# recursividade com Fibonacci
# complexidade O(2ⁿ) -> cresce exponencialmente
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n -1) + fibonacci(n -2)

# programa principal
x = fibonacci(5)
print(x)
