quant_notas = int(input("Digite a quantidade de notas do trimestre:"))
media = 0
if quant_notas > 10:
    print("O número de notas é muito alto, o máximo é igual a 10 notas")
    quant_notas = int(input("Digite a quantidade de notas do trimestre:"))

for i in range(quant_notas):
    notas = float(input("Digite as notas do aluno:"))
    media += notas

media = media / quant_notas
print(media)