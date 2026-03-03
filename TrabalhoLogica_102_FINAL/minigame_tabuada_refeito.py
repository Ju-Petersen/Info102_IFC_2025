import random
import json
import time

#print("O minigame vai começar! \n Digite a resposta correta no campo abaixo e tente responder corretamente o mais rápido possível!")

lst_pontos = []
#def jogar(), função que contém o minigame de multiplicação. Randomizando os números de 0 a 10.    
def jogar():
    max_erros = 5
    erros_jogo = 0
    pontos_jogo = 0
    
    for i in range(10):
        n1 = random.randint(0, 10)  #O random gera números aleatórios entre 0-10 para mostrar ao usuário
        n2 = random.randint(0, 10)
        resp_certa = n1 * n2
        print(n1, "x", n2)
        resp_usuario = int(input("Resposta: "))
        while resp_usuario != resp_certa:
            if pontos_jogo == 0:
                erros_jogo += 1
                print("Pontuação: ", pontos_jogo, " Erros: ", erros_jogo)
            else:
                pontos_jogo -= 100
                erros_jogo += 1
                print("Pontuação: ", pontos_jogo, " Erros: ", erros_jogo)
            break
        while resp_usuario == resp_certa:
            pontos_jogo += 100
            print("Pontuação: ", pontos_jogo, " Erros: ", erros_jogo)
            break
        
        if erros_jogo == max_erros:
                print("Você atingiu ", max_erros, " erros. Fim de jogo!")
                break
    
    lst_pontos.append(pontos_jogo)  
    print("\nFim do jogo!", "Sua pontuação final foi: ", pontos_jogo)

#-----------------------------------------------------------------------------------------------------------#
#def cadastrar(nome_usuario), função que realiza o cadastro do usuário, este método utilizado, com o parâmetro "nome_usuario" possibilitou a utilização do "resgate" dessa variável para o ranking.

#Parâmetro "nome_usuario": Este é o nome que o usuário irá digitar para aparecer no ranking e é o nome que será relacionado à pontuação específica daquele usuário, (é também a variável onde o usuário digita seu nome de usuário antes do início do jogo justamente para realizar essa relação).

usuarios = []
def cadastrar(nome_usuario):
    usuarios.append(nome_usuario)
    print("Usuário cadastrado com sucesso!")

#-----------------------------------------------------------------------------------------------------------#
#def adicionar_dados_ranking(lst_ranking): função que é utilizada para "resgatar" os dados do nome_usuario e pontos_jogo para aparecerem no ranking (este, que é o dicionário).

#Parâmetro "lst_ranking": é a lista/dicionário criada para salvar os dados de "usuarios" relacionados com suas posições respectivas de "lst_pontuacao". É utilizado em lista para a disposição de cada linha abaixo da outra no "arquivo_do_ranking.txt"

def adicionar_dados_ranking(lst_ranking):
    lst_ranking = []
    for i in range(len(lst_pontos)):
        lst_ranking.append({"Nome": usuarios[i], "Pontos": lst_pontos[i]})
    return lst_ranking

#-----------------------------------------------------------------------------------------------------------#
#def organizar_inserton_sort(lst_ranking): função que ordena o ranking em ordem decrescente de acordo com a pontuação.

#Parâmetro "lst_ranking": lista com o dicionário que possui o ranking gravado.

def organizar_inserton_sort(lst_ranking):
    for i in range(0, len(lst_ranking)):
        for k in range(i, 0, -1):
            if lst_ranking[k - 1]["Pontos"] < lst_ranking[k]["Pontos"]:
                aux = lst_ranking[k]
                lst_ranking[k] = lst_ranking[k - 1]
                lst_ranking[k - 1] = aux
            else:
                break
    return lst_ranking

#-----------------------------------------------------------------------------------------------------------#
#def procurar(pontuacao_procurada): função que é utilizada para encontrar qualquer usuário que estiver cadastrado. Possibilita outros usuários a encontrarem duas pontuações mais facilmente, localizando também outros usuários que tenham a mesma pontuação.

#Parâmetro "pontuacao_procurada": o usuário digita uma pontuação determinada e são mostrados toos os usuários que possuem a mesma pontuação.

def procurar(pontuacao_procurada):
    lst_ranking = adicionar_dados_ranking(usuarios)
    achou = False
    for i in lst_ranking:
        if i["Pontos"] == pontuacao_procurada:
            print("Nome:", i["Nome"], "- Pontos:", i["Pontos"])
            achou = True
    if not achou: #Comando "not", utilizado para inverter a condição, nesse caso, se "achou" for False, a condição do if será verdadeira (se "achou" não se tornou verdadeira, a condição do if é satisfeita)
        print("Nenhum usuário encontrado com essa pontuação.")

def main():
    selecao = int(input('''
#-----------------------------------#
| 1 - Iniciar minigame              |
| 2 - Cadastrar usuário             |
| 3 - Procurar usuário por pontos   |
| 4 - Visualizar Ranking            |
| 5 - Sair                          |
#-----------------------------------#
Selecione uma das opçôes do menu acima (de 1 até 5):
          '''))
    
    if selecao == 1:
        #Comandos não vistos em aula e aqui utilizados (in e not in), fazem o papel de ler a lista "usuários" e verificar se o valor digitado pelo usuário já foi utilizado na lista ou não. Estes comandos facilitam este processo de ler todas as posições da lista e verificar se o valor é repetido ou não.
        nome_usuario = input("Se você já foi cadastrado, digite o seu nome de ususário: ")
        if nome_usuario in usuarios:
            print("Ok, se prepare para o minigame", nome_usuario, "!")
            jogar()
            print("\n IMPORTANTE: Caso você tenha realizado o cadastro, e deseja que sua pontuação apareça no ranking, vá até o item 4 do menu principal para salvar sua pontuação no ranking! (Aguarde até que o menu reecarregue).")
            time.sleep(5)
            main()
        elif nome_usuario not in usuarios:
            aviso_jogo = input('''\n Parece que você não está cadastrado.

Caso você tenha digitado seu nome de usuário errado, digite T para tentar novamente. 
Digite C para se cadastrar antes de jogar, ou J para jogar sem cadastro: ''')
            
            if aviso_jogo == "C" or aviso_jogo == "c":
                nome_usuario = input("Digite o nome de usuário que deseja cadastrar: ")
                while nome_usuario in usuarios:
                    nome_usuario = input("Esse nome de usuário já existe. Tente novamente: ")
                if nome_usuario not in usuarios:
                    cadastrar(nome_usuario)
                    print("\n Ok, se prepare para o minigame", nome_usuario, "!")
                    jogar()
                    print("\n IMPORTANTE: Caso você tenha realizado o cadastro, e deseja que sua pontuação apareça no ranking, vá até o item 4 do menu principal para salvar sua pontuação no ranking! (Aguarde até que o menu reecarregue).")
                    time.sleep(5)
                    main()
            
            elif aviso_jogo == "J" or aviso_jogo == "j":
                jogar()
                time.sleep(0.5)
                main()
            
            elif aviso_jogo == "T" or aviso_jogo == "t":
                nome_usuario = input("\n Se você já foi cadastrado, digite o seu nome de ususário: ")
                if nome_usuario in usuarios:
                    print("\n Ok, se prepare para o minigame", nome_usuario, "!")
                    jogar()
                    print("\n IMPORTANTE: Caso você tenha realizado o cadastro, e deseja que sua pontuação apareça no ranking, vá até o item 4 do menu principal para salvar sua pontuação no ranking! (Aguarde até que o menu reecarregue).")
                    time.sleep(5)
                    main()
        else:
            print("Opção inválida. Voltando ao menu principal.")
            main()
    
    elif selecao == 2:
        nome_usuario = input("Digite o nome de usuário que deseja cadastrar: ")
        while nome_usuario in usuarios:
            input("Esse nome de usuário já existe. Tente novamente: ")
        if nome_usuario not in usuarios:
            cadastrar(nome_usuario)
            main()
    
    elif selecao == 3:
        pontuacao_procurada = int(input("Digite a pontuação aqui: "))
        procurar(pontuacao_procurada)
        main()
    
    if selecao == 4:
        
        arquivo = open("arquivo_do_ranking.txt", "w", encoding="utf-8")
        lst_ranking = adicionar_dados_ranking(usuarios)
        
        lst_ranking = organizar_inserton_sort(lst_ranking) #Observação: A função de ordenação do ranking deve ser colocada antes do json.dumps para que os dados possam ser salvos na ordem desejada. (Comentado isso, pois causou confusão no processo de desenvolvimento do algoritmo)
        
        lst_ranking_json = json.dumps(lst_ranking)
        lst_ranking_json = lst_ranking_json.replace("},", "},\n")
    
        arquivo.write(lst_ranking_json)
        arquivo.close()
        print("Dados Salvos!")
    
        arquivo = open("arquivo_do_ranking.txt", "r", encoding="utf-8")
        print(arquivo.read())
        arquivo.close()
    
        menu = input("Pressione E para voltar ao menu: ")
        if menu == "E" or menu == "e":
            main()
        else:
            print("Ops! Algo deu errado, aguarde o menu recarregar.")
            time.sleep(1)
            main()

    elif selecao == 5:
        print("O programa foi encerrado!")
        
    elif selecao < 1 or selecao > 5:
        print("Ops! Algo deu errado, aguarde o menu recarregar.")
        time.sleep(1)
        main()

main()

#Observação: Para este código foram utilizados modelos de outros códigos já corrigidos/feitos em outras aulas. (Principalmente na parte que deve gravar e recuperar dados). O uso de comandos não estudados em sala, como o "in", "not" e "not in" foram compreendidos após pesquisas sobre suas funcionalidades e como podem ser utilizados, apesar disso o uso de outras fontes (como fóruns e IA) não foi copiado e sim compreendido para ser aproveitado no funcionamento deste algoritmo.