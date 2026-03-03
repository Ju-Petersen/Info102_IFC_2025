n = int(input("Digite um número qualquer:"))
divisivel = 0

for i in range(n):
    if i % 3 == 0:
        divisivel += 1
print(divisivel)