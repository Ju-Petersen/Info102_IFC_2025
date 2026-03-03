maior = 0
numeros = []

for i in range(20):
    numeros.append(int(input("Digite um número qualquer:")))
    if numeros[i] > maior:
        maior = numeros[i]
        
print("O maior número é:", maior)