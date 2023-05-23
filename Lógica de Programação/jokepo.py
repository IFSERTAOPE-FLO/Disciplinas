# Jo Ke Po
import random
import time
'''
Pedra, papel, tesoura, lagarto e spock
Regras:
- Pedra ganha da tesoura (amassando-a ou quebrando-a).
- Tesoura ganha do papel (cortando-o).
- Papel ganha da pedra (embrulhando-a).
- Lagarto ganha do Spock (envenenando-o).
- Spock ganha da tesoura (quebrando-a).
- Tesoura ganha do lagarto (decapitando-o).
- Lagarto ganha do papel (comendo-o).
- Papel ganha de Spock (desmentindo-o).
- Spock ganha da pedra (vaporizando-a).
- Pedra ganha do lagarto (esmagando-o).
- Se dois jogadores fizerem a mesma escolha, ocorre um empate.
- 2 jogadores: você e o computador
'''
def inicio():
    print("=-" * 30)
    print("Bem-vindos ao JO KE PO!")
    print("=-" * 30)
    print("Escolha sua opção")
    print("1: Pedra, 2: Tesoura 3: Papel 4: Lagarto 5: Spock")
    pc = random.randint(1, 5)
    user = int(input())
    # win = user Ganhou / lose = PC ganhou / empate
    ganhador = compara(user, pc)
    print("JO", end=" ")
    time.sleep(1)
    print("KE", end=" ")
    time.sleep(1)
    print("PO", end=" ")
    time.sleep(1)
    print()
    winner(ganhador)

def winner(ganhador):
   if ganhador == "win":
       print("O usuário ganhou!")
   elif ganhador == "lose":
       print("O compudador ganhou!")
   else:
       print("Houve um empate!")

def compara(opUser, opPc):
    if opUser == opPc:
        return "empate"
    elif opUser == 1 and opPc == 2 or opUser == 1 and opPc == 4:
        return "win"
    elif opUser == 1 and opPc == 3 or opUser == 1 and opPc == 5:
        return "lose"
    elif opUser == 2 and opPc == 1 or opUser == 2 and opPc == 4:
        return "lose"
    elif opUser == 2 and opPc == 3 or opUser == 2 and opPc == 5:
        return "win"
    elif opUser == 3 and opPc == 1 or opUser == 3 and opPc == 5:
        return "win"
    elif opUser == 3 and opPc == 2 or opUser == 3 and opPc == 4:
        return "lose"
    elif opUser == 4 and opPc == 2 or opUser == 4 and opPc == 3:
        return "win"
    elif opUser == 4 and opPc == 1 or opUser == 4 and opPc == 5:
        return "lose"
    elif opUser == 5 and opPc == 1 or opUser == 5 and opPc == 3:
        return "win"
    elif opUser == 5 and opPc == 2 or opUser == 5 and opPc == 4:
        return "lose"

jogar = True
while(jogar):
    inicio()
    ent = int(input("Digite 1 para jogar de novo ou qualquer "
          "outro número para encerrar."))
    if ent != 1:
        jogar = False
print("Fim de jogo!")
# Criar campeonatos ou jogos avulsos
# Campeonato: pode definir quantas partidas terão
# Ao final do campeonato, apresentar o placar
# Obs.: Para guardar informações, recomenda-se o uso de listas