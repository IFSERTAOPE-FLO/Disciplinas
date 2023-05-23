# Faça um programa que leia do usuário dois vetores de 3 posições, que representam 
# forças sobre um ponto no espaço 3D, e escreva a força resultante

lista1 = []
lista2 = []
for i in range(3):
    lista1.append(int(input("Digite um valor para a lista 1: ")))
for i in range(3):
    lista2.append(int(input("Digite um valor para a lista 2: ")))
forca_resultante = []
for i in range(len(lista1)):
    forca_resultante.append(lista1[i] + lista2[i])
print(forca_resultante)
