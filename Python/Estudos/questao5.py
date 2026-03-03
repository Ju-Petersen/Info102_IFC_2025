numero_notas = int(input("Digite a quantidade de notas do aluno:"))
media = 0

if numero_notas > 10:
    numero_notas = int(input("Digite a quantidade de notas do aluno, no máximo, 10:"))

for i in range (numero_notas):
    notas = float(input("Digite a nota do aluno:"))
    media = media + notas

print(media/numero_notas)