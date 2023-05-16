# Faça um programa para determinar o número de dígitos de um número
# inteiro positivo informado (usando for)

num = int(input("digite um número inteiro positivo"))
cont = 0
while num > 0:
    num = num // 10
    cont = cont + 1
print("o número tem", cont, "dígitos")

# usando for
num = int(input("digite um número inteiro positivo"))
cont = 0
for i in range(num):
    if num == 0:
        break
    num = num // 10
    cont = cont + 1
print("o número tem", cont, "dígitos.")
