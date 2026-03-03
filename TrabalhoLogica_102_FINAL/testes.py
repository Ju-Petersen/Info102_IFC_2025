#Dicionário: 'variavel = {"Nome:" variavel, "Nome:"}' ou 'variavel.append({"Nome:" variavel, "Nome:"})'

#-------------------------------------------------------------------------------------------------------------------------#

#Esta solução (entre as demarcações) não foi útil.

#elif selecao == 3:
        #nome_procurado = input("Digite o nome do usuário que deseja procurar: ")
        #if nome_procurado in ranking:
            #print(f"Usuário encontrado: {nome_procurado}")
            #print(f"Pontuação: {ranking[nome_procurado]} pontos")
        #else:
            #print("Usuário não encontrado.")
        #main()

    #elif selecao == 4:
        #if not ranking:
            #print("Nenhum jogador registrado ainda.")
        #else:
            #print("\n===== RANKING GERAL =====")
            #for pos, (nome, pontos) in enumerate(sorted(ranking.items(), key=lambda x: x[1], reverse=True), start=1):
                #print(f"{pos}º - {nome}: {pontos} pontos")
                
#-------------------------------------------------------------------------------------------------------------------------#

def adicionar_dados_ranking(nome_usuario, pontos_jogo):
    usuarios = nome_usuario.split(",")
    ranking = {"Nome": usuarios, "Pontos": pontos_jogo}
    return ranking

#-------------------------------------------------------------------------#

def ordenar(nome_usuario):
    for i in ranking:
        for k in i["Nome"]:
            if k == nome_usuario:
               print(i)
               
#-------------------------------------------------------------------------#
            
def procurar(pontuacao_procurada):
    achou = False
    for i["Pontos"] in lst_ranking:
            if i["Pontos"] == pontuacao_procurada:
                print("Usuário:", i["Nome"], "- Pontos:", i["Pontos"])
                achou = True
            elif achou == False:
                print("Ainda não há ninguém com essa pontuação.")
    return print(pontuacao_procurada) #sem return + colocar def adicionar_dados_ranking(usuarios) dentro, para que não seja procurado dentro de uma lista vazia (lst_ranking = []).