preco_carro = float(input())

poupanca = 10000.0
meses = 0

while poupanca < preco_carro:
    poupanca += poupanca * 0.007
    preco_carro += preco_carro * 0.004
    meses += 1

print(meses)
