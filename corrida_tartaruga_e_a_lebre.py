distancia_tartaruga = int(input())
distancia_lebre = 0
minutos = 0

while distancia_lebre < distancia_tartaruga:
    distancia_tartaruga += 1
    distancia_lebre += 10
    minutos += 1

print(minutos)
