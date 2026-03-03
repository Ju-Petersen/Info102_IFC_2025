lst_numero = []

for i in range(5):
    lst_numero.append(float(input("Digite um número qualquer:")))

procurar = float(input("Digite qual número da lista você quer encontrar:"))

if procurar == lst_numero[i]:
    print("O número:", procurar, " foi encontrado na lista.")
else:
    print("O número não foi encontrado na lista.")