while True:
    lst = []

    hora = input("Digite o horário que você quer converter (HH:MM): ")
    lst = hora.split(":")
    lst.append(hora)

    def converter_hora(hora):
            return hora - 12
        
    def imprimir_hora(hora=hora):
        hora = int(lst[0])
        if hora > 12:
            hora = converter_hora(hora)
            return print(hora, ":", lst[1], "P.M")
        elif hora == 00:
            return print(12, ":", lst[1], "A.M")
        elif hora < 12:
            return print(hora, ":", lst[1], "A.M")

    imprimir_hora(hora)
