lista_numeros = []
i = 0

for i in range(5):
    lista_numeros.append(int(input("Digite um número qualquer:")))

numero_usuario = int((input("Digite um número que quer procurar na lista:")))

if numero_usuario == lista_numeros[i]:
    print("O número está na lista.")
else: 
    print("O número não está na lista.")

