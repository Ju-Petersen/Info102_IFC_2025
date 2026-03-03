cobre = float(input("Digite a quantidade de cobre da peça:"))
zinco = float(input("Digite a quantidade de zinco da peça:"))
estanho = float(input("Digite a quantidade de estanho da peça:"))
total_peca = cobre + zinco + estanho

porcentagem = (cobre / total_peca) * 100
print(porcentagem)