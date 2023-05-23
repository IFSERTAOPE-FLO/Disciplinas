import random
# Matrizes

#vetor
pokemons_agua = ['squirtle', 'psyduck', 'magikarp', 'lapras', 'vaporeon']
pokemons_fogo = ['charmander', 'vulpix', 'flareon', 'magmar', 'moltres']
pokemons_grama = ['bulbasaur', 'oddish', 'bellsprout', 'exeggcute', 'vileplume']

#matriz
pokemons = [pokemons_agua, pokemons_fogo, pokemons_grama]
for pok in pokemons:
    for pk in pok:
        print(pk)

# matriz 15x15
exemplo = [
    [0] * 15,
] * 15
for linha in exemplo:
        for coluna in linha:
            print(coluna, end=" ")
        print()

linha = random.randint(0,15)
coluna = random.randint(0,15)
exemplo[linha][coluna] = 1

for linha in exemplo:
        for coluna in linha:
            print(coluna, end=" ")
        print()