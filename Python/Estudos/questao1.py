ultimo_n = 1
penultimo_n = 0

n_atual = penultimo_n + ultimo_n

while n_atual < 500:
    print(n_atual)
    penultimo_n = ultimo_n
    ultimo_n = n_atual
    n_atual = penultimo_n + ultimo_n
    print(n_atual)
