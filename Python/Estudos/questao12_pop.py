cpf = []
nomes = []

for i in range (3):
    nomes.append(input("Digite o nome do cliente: "))

for i in range (3):
    cpf.append(input("Digite o CPF do cliente: "))
    
deletar = int(input("Digite aposição do cliente que você quer deletar: "))

cpf.pop(deletar)
nomes.pop(deletar)

print(nomes)
print(cpf)

#Método gambiarra:
    #cpf = []
    #nomes = []

    #for i in range (3):
        #nomes.append(input("Digite o nome do cliente: "))

    #for i in range (3):
        #cpf.append(input("Digite o CPF do cliente: "))

    #deletar = int(input("Digite aposição do cliente que você quer deletar: "))
    #cpf[deletar] = ""
    #nomes[deletar] = ""

    #for i in range (3):
        #print(nomes[i], cpf[i])