p1 = int(input())
p2 = int(input())

pop_a = max(p1, p2)
pop_b = min(p1, p2)

anos = 0

while pop_b <= pop_a:
    pop_a += pop_a * 0.02
    pop_b += pop_b * 0.03
    anos += 1

print(anos)
