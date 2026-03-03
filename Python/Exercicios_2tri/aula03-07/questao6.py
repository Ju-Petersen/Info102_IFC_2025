numero1 = float(input("Digite um número qualquer:"))
numero2 = float(input("Digite outro número qualquer:"))
numero3 = float(input("Digite mais um número qualquer:"))
if numero1 > numero2 and numero1 > numero3:
    print("O maior número é:" , numero1)
elif numero2 > numero1 and numero2 > numero3:
    print("O maior número é:" , numero2)
else:
    print("O maior número é:" , numero3)