numeros = []
i = 0

for i in range (20):
    numeros.append(int(input("Digite números aleatórios:")))

for i in range(numeros[i]):
    if numeros[i] == numeros[i-1]:
        print("O número", numeros[i], "é repetido na lista.")
 