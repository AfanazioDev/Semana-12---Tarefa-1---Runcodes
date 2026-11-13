data = int(input())

soma = 0

while data > 0:
  digito = data % 10
  soma += digito
  data //= 10

print(soma)
