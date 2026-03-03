numeros = 0
negativos = 0
cont = 0

while cont < 10:
    cont += 1
    numeros = int(input("Digite números inteiros positivos e negativos:"))
    if numeros < 0:
        negativos += 1
        
print(negativos)