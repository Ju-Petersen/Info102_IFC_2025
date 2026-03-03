nome_clientes = []
gasto_clientes = []
bonus = 0

for i in range (3):
    nome_clientes.append(input("Digite o nome dos clientes:"))
    
for i in range (3):
    gasto_clientes.append(float(input("Digite o gasto dos clientes:")))

for i in range (3):
    bonus = (gasto_clientes[i] / 100) * 2
    print(nome_clientes[i], bonus)