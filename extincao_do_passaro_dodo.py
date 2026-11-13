populacao_inicial = int(input())
populacao_atual = populacao_inicial
limite = populacao_inicial * 0.10
ano = 1600

while populacao_atual >= limite:
    nascimentos = populacao_atual * 0.01
    mortes = populacao_atual * 0.06
    populacao_atual = populacao_atual + nascimentos - mortes

    print(f"{ano},{round(nascimentos)},{round(mortes)},{round(populacao_atual)}")
    ano += 1
