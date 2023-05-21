# Faça um programa para calcular a série de
# Fibonacci para um número informado pelo usuário,
# sendo F(0) = 0, F(1) = 1 e F(n)= F(n-1)+F(n-2)

def fibonacci(num):
    num = int(input("Digite um número"))
    a = 0
    b = 1
    for i in range(num):
        print(a)
        c = a + b
        a = b
        b = c
