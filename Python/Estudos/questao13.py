numeros = []
numeros.append(float(input("Digite um numero qualquer:")))
maior = 0

for i in range(2):
    numeros.append(float(input("Digite um numero qualquer:")))
    if numeros[i + 1] > numeros[i]:
        maior = numeros[i + 1]

print(maior)