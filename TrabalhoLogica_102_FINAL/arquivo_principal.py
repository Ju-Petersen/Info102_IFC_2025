import random
import json
import time

lst_pontuacao = []
lst_ranking = []

#def jogar(), função que contém o minigame de multiplicação. Randomizando os números de 0 a 10.
def jogar():
    print('''
O minigame vai começar! 
Digite a resposta correta no campo abaixo e tente responder corretamente o mais rápido possível!
          ''')
    iniciar = input("(Digite 'A' para começar): ")
    max_erros = 5
    max_acertos = 10
    erros_jogo = 0
    acertos_jogo = 0
    pontos_jogo = 0
    rodadas = 0

    while iniciar == "a" or iniciar == "A":
        if rodadas == 0:
            n1 = random.randint(0, 10)  #O random gera números aleatórios entre 0-10 para mostrar ao usuário
            n2 = random.randint(0, 10)
            resp_certa = n1 * n2
            print(n1, "x", n2)
            resp_usuario = int(input("Resposta: "))

            if resp_usuario == resp_certa:
                acertos_jogo += 1
                pontos_jogo += 100
                print("Pontuação Final: ", pontos_jogo, "Erros totais: ", erros_jogo)
            elif resp_usuario != resp_certa:
                erros_jogo += 1
                print("Pontuação Final: ", pontos_jogo, "Erros totais: ", erros_jogo)
                if resp_usuario != resp_certa and pontos_jogo > 0:
                    pontos_jogo -= 100
                    print("Pontuação Final: ", pontos_jogo, "Erros totais: ", erros_jogo)
            if erros_jogo == max_erros:
                print("Você cometeu", max_erros, "O jogo acabou!")
                main()
                break
            elif acertos_jogo == max_acertos:
                print("Parabéns, você chegou ao limite do minigame, com 10 acertos! \n", "Pontuação Final: ", pontos_jogo, "Erros totais: ", erros_jogo)
                lst_pontuacao.append(pontos_jogo)
                rodadas +=1
                print("\n IMPORTANTE: Caso você tenha realizado o cadastro, e deseja que sua pontuação apareça no ranking, vá até o item 4 do menu principal para salvar sua pontuação no ranking! (Aguarde até que o menu reecarregue).")
                time.sleep(5)
                main()
        elif rodadas >= 1:
            break
        
#-----------------------------------------------------------------------------------------------------------#

#def cadastrar(nome_usuario), função que realiza o cadastro do usuário, este método utilizado, com o parâmetro "nome_usuario" posssibilitou a utilização do "resgate" dessa variável para o ranking, porém a mesma solução não foi encontrada com a variável pontos_jogo.
usuarios = []
def cadastrar(nome_cadastro):
    opcao_cadastro = True
    
    while opcao_cadastro == True:       
        if opcao_cadastro == True:
            nome_cadastro = input("Digite novamente o nome de usuário: ")
            if nome_cadastro not in usuarios:
                usuarios.append(nome_cadastro)
                print("Usuário", nome_cadastro, "cadastrado.")
                opcao_sair = input("Deseja sair? (digite S para sair): ")
                if opcao_sair == "S" or opcao_cadastro == "s":
                    main()
                else:
                    main()
            elif nome_cadastro in usuarios:
                while nome_cadastro in usuarios or nome_cadastro == "":
                    nome_cadastro = input("Este usuário já existe, ou é inválido. Digite um novo nome de usuário: ")
                    #Comandos não vistos em aula e aqui utilizados (in e not in), fazem o papel de ler a lista "usuários" e verificar se o valor digitado pelo usuário já foi utilizado na lista ou não. Estes comandos facilitam este processo de ler todas as posições da lista e verificar se o valor é repetido ou não.
                    if nome_cadastro not in usuarios and nome_cadastro != "":
                        usuarios.append(nome_cadastro)
                        print("Usuário", nome_cadastro, "cadastrado.")
                        opcao_sair = input("Deseja sair? (digite S para sair): ")
                        if opcao_sair == "S" or opcao_cadastro == "s":
                            main()
                        else:
                            main()
                        break
        elif nome_cadastro == "":
            nome_cadastro = input("Nome inválido. Digite um nome de usuário: ")
        
        opcao_cadastro = False            
        if opcao_cadastro == False:
            break

#-----------------------------------------------------------------------------------------------------------#

def adicionar_dados_ranking(lst_ranking):
    lst_ranking = []
    for i in range(len(lst_pontuacao)):
        lst_ranking.append({"Nome": usuarios[i], "Pontos": lst_pontuacao[i]})
    return lst_ranking

#-----------------------------------------------------------------------------------------------------------#

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

#função que é utilizada para encontrar qualquer usuário que estiver cadastrado. Possibilita outros usuários a encontrarem duas pontuações mais facilmente, localizando também outros usuários que tenham a mesma pontuação.

def procurar(pontuacao_procurada):
    lst_ranking = adicionar_dados_ranking(usuarios)
    achou = False
    for i in lst_ranking:
        if i["Pontos"] == pontuacao_procurada:
            print("Nome:", i["Nome"], "- Pontos:", i["Pontos"])
            achou = True
    if not achou: #Comando "not", utilizado para inverter a condição, nesse caso, se "achou" for False, a condição do if será verdadeira (se "achou" não se tornou verdadeira, a condição do if é satisfeita)
        print("Nenhum usuário encontrado com essa pontuação.")
        
#Observação: foi preciso utilizar a função adicionar_dados_ranking(usuarios) dentro da função, para que não seja feita a procura em uma lista vazia (lst_ranking = []). (Comentado isso, pois causou confusão no processo de desenvolvimento do algoritmo)

#-----------------------------------------------------------------------------------------------------------#

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
        nome_usuario = input("Se você já foi cadastrado, digite o seu nome de ususário: ")
        if nome_usuario in usuarios:
            print("Ok, se prepare para o minigame", nome_usuario, "!")
            jogar()
        elif nome_usuario not in usuarios and nome_usuario != "":
            aviso_jogo = input('''Parece que você não está cadastrado.

Caso você tenha digitado seu nome de usuário errado, digite T para tentar novamente.
            
Digite C para se cadastrar antes de jogar.

Ou digite J para jogar sem cadastro: ''')
            if aviso_jogo == "C" or aviso_jogo == "c":
                cadastrar(nome_cadastro=nome_usuario)
            elif aviso_jogo == "J" or aviso_jogo == "j":
                jogar()
            elif aviso_jogo == "T" or aviso_jogo == "t":
                nome_usuario = input("Se você já foi cadastrado, digite o seu nome de ususário: ")
                if nome_usuario in usuarios:
                    print("Ok, se prepare para o minigame", nome_usuario, "!")
                    jogar()

    elif selecao == 2:
        nome_usuario = input("Digite o nome de usuário que deseja cadastrar: ")
        cadastrar(nome_cadastro=nome_usuario)

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