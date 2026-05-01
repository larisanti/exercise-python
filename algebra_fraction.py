"""
Curso: 
College Algebra with Python (freeCodeCamp)

Objetivo: 
Utilizar um script em Python para praticar a resolução de equações com números inteiros, decimais e frações.

Notes:
Não fiz o código, apenas estudei como foi construído e resolvi os problemas 
(que foi o que o professor recomendou).

Achei muito interessante quando o professor aplicou a mesma operação dos dois lados do sinal de =.
Eu costumava resolver só de um lado, isolando o x e pulando uma etapa.
Entendi que essa lógica é importante para trabalhar com algoritmos, mas ainda está abstrato. 

Minhas respostas:

21
33
1.67
90
27
6
19
0.25
120
2.78
1.90
17

Acertei 8/12 (preciso praticar mais)

Adorei resolver problemas de matemática assim, nem vi o tempo passar :) 
São exercícios infinitos, vou refazer até acertar todos os 12 primeiros. 
"""


# Run this code to practice solving one-step and two-step problems.
# It will give you 12 practice problems.
# If you don't get them all correct, you can run this again to get more practice.
# Your answer can be a fraction, decimal, or whole number.

# Converts string input (even fractions) to float
def string_frac(in_string):
    if "/" in in_string:
        nd = in_string.split("/")
        n = float(nd[0])
        d = float(nd[1])
        ans = n/d
        return ans
    else:
        ans = float(in_string)
        return ans


# Simplest one-step addition
def one_step_add():
    import random
    # Display problem
    a = random.randint(-4,10)
    b = random.randint(2,24)
    print("x + ", a, " = ", b)
    ans = float(input("x = "))
    answer = b-a
    # Test input
    if ans==answer:
        print("Correct! \n")
    else:
        print("Try again")
        print("The correct answer is ", answer, "\n")


# One-step additon with negative numbers
def one_step_subtract():
    import random
    a = random.randint(-19,-1)
    b = random.randint(2,24)
    print(a, " + x = ", b)
    ans = float(input("x = "))
    # test
    answer = b-a
    if ans==answer:
        print("Correct! \n")
    else:
        print("Try again")
        print("The correct answer is ", answer, "\n")

# One-step multiply
def one_step_mult():
    # Uses string_frac(<input string>)
    import random
    a = random.randint(1,11)
    b = random.randint(2,24)
    print(a, "x = ", b)
    print("Round your answer to two decimal places.")
    ans_in = (input("x = "))
    answer = round(b/a,2)
    # test
    if string_frac(ans_in)==answer:
        print("Correct! \n")
    else:
        print("Try again")
        print("The correct answer is ", answer, "\n")


# One-step divide
def one_step_div():
    import random
    a = random.randint(1,11)
    b = random.randint(2,24)
    print("x/", a, " = ", b)
    ans = float(input("x = "))
    answer = b*a
    # test
    if ans==answer:
        print("Correct! \n")
    else:
        print("Try again")
        print("The correct answer is ", answer, "\n")


# Two-step problems
def two_step():
    import random
    # Uses string_frac()
    a = random.randint(1,11)
    b = random.randint(-7,12)
    c = random.randint(2,36)
    print(a, "x + ", b, " = ", c)
    print("Round answer to two decimal places")
    ans_in = input("x = ")
    answer = (c-b)/a
    # test
    if round(string_frac(ans_in),2)==round(answer,2):
        print("Correct! \n")
    else:
        print("Try again")
        print("The correct answer is ", answer, "\n")


# Test loop
for a in range(2):
    one_step_add()
    one_step_subtract()
    one_step_mult()
    one_step_div()
    two_step()
    print(" ")

two_step()
two_step()
