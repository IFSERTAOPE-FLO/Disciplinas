import random

# Equipes
equipes = ["Equipe A", "Equipe B", "Equipe C", "Equipe D", "Equipe E"]

# Sorteio dos confrontos
confrontos = []
for i in range(len(equipes)):
    for j in range(i + 1, len(equipes)):
        confrontos.append((equipes[i], equipes[j]))

# Sorteio das perguntas
perguntas_disponiveis = list(range(1, 79))
perguntas_confrontos = {}
for confronto in confrontos:
    perguntas_confronto = random.sample(perguntas_disponiveis, 5)
    perguntas_confrontos[confronto] = perguntas_confronto
    for pergunta in perguntas_confronto:
        perguntas_disponiveis.remove(pergunta)

# Simulação dos confrontos e contagem dos pontos
pontuacao = {equipe: 0 for equipe in equipes}
for confronto in confrontos:
    equipe1, equipe2 = confronto
    print(f"{equipe1} vs {equipe2}")
    for pergunta in perguntas_confrontos[confronto]:
        print(f"Pergunta {pergunta}:")
        resposta_equipe1 = input(f"{equipe1}, você quer responder (r) ou passar (p)? ")
        if resposta_equipe1 == "r":
            resposta = input(f"{equipe1}, responda à pergunta: ")
            # Aqui você pode adicionar lógica para validar a resposta e atribuir pontos
            if resposta == "correta":
                pontuacao[equipe1] += 1
                break
        resposta_equipe2 = input(f"{equipe2}, você quer responder (r) ou passar (p)? ")
        if resposta_equipe2 == "r":
            resposta = input(f"{equipe2}, responda à pergunta: ")
            # Aqui você pode adicionar lógica para validar a resposta e atribuir pontos
            if resposta == "correta":
                pontuacao[equipe2] += 1
                break

# Classificação final
classificacao = sorted(pontuacao.items(), key=lambda x: x[1], reverse=True)
print("\nClassificação Final:")
for i, (equipe, pontos) in enumerate(classificacao):
    print(f"{i+1}. {equipe}: {pontos} pontos")

# Enfrentamento das duas melhores equipes
melhores_equipes = [classificacao[0][0], classificacao[1][0]]
print(f"\nEnfrentamento entre {melhores_equipes[0]} e {melhores_equipes[1]}")

# Sorteio das perguntas para o enfrentamento
perguntas_enfrentamento = random.sample(perguntas_disponiveis, 5)

# Simulação do enfrentamento
pontuacao_enfrentamento = {equipe: 0 for equipe in melhores_equipes}
for pergunta in perguntas_enfrentamento:
    print(f"Pergunta {pergunta}:")
    resposta_equipe1 = input(f"{melhores_equipes[0]}, responda à pergunta: ")
    if resposta_equipe1 == "correta":
        pontuacao_enfrentamento[melhores_equipes[0]] += 1
    resposta_equipe2 = input(f"{melhores_equipes[1]}, responda à pergunta: ")
    if resposta_equipe2 == "correta":
        pontuacao_enfrentamento[melhores_equipes[1]] += 1

# Classificação final do enfrentamento
classificacao_enfrentamento = sorted(
    pontuacao_enfrentamento.items(), key=lambda x: x[1], reverse=True
)
print("\nClassificação do Enfrentamento:")
for i, (equipe, pontos) in enumerate(classificacao_enfrentamento):
    print(f"{i+1}. {equipe}: {pontos} pontos")
