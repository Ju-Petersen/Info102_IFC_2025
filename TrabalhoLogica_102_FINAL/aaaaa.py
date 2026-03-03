#Ideia de timer excluída, com as ferramentas ensinadas até agora, não foi possível encontrar uma solução para a implementação do timer, devido ao limite de entrega do trabalho esta parte foi desconsiderada como essencial, e não será implementada.

import time

minutos = 0
segundos = 60
total_segundos = minutos * 60 + segundos
   
while total_segundos > 0:
    minutos, segundos = divmod(total_segundos, 60)
    texto_tempo = f'{minutos:02d}:{segundos:02d}'
    time.sleep(1)
    print(texto_tempo, end='\r')
    total_segundos -= 1

# Observação: o código comentado abaixo é a versão do timer como função.

# def marcar_tempo(minutos, segundos):
    #total_segundos = minutos * 60 + segundos
   
    #while total_segundos > 0:
        #minutos, segundos = divmod(total_segundos, 60)
        #texto_tempo = f'{minutos:02d}:{segundos:02d}'
        #time.sleep(1)
        #print(texto_tempo, end='\r')
        #total_segundos -= 1

#marcar_tempo(0, 60)

#___________________________________________________________________________________________________

