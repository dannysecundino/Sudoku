import functions as fu                      # Estamos importando as funções do arquivo "functions.py"
import sys                                  # Importando a biblioteca para 
arquivos = sys.argv                         # Esta lendo as informações dadas no terminal
arquivo = open(arquivos[1], "r")            # Esta abrindo o arquivo com o nome dado no terminal
linhas = arquivo.readlines()        
for coordenadas in linhas:                  # Estamos percorrendo todas as linhas do arquivo aberto
    coordenadas = fu.formata(coordenadas)   # Transformando as coordenadas em uma lista
    fu.setPista(coordenadas[1], coordenadas[0], coordenadas[2]) # Adicionando as pistas na matriz principal do jogo
fu.tabelaSudoku("")                           # A tabela ja sera printada com as pistas
  

while True:     #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Provisorio!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    entrada = input("       Digite a sua entrada: ")
    entrada = fu.formata(entrada)
    #print(entrada)
    l = entrada[1]
    c = entrada[0]
    if entrada[2] == '!':   # Para excluir uma posicao
        if fu.pista[l][c]:                                             # Pistas nao podem seer excluidas
            alerta = "Nao se pode excluir uma pista!"
        elif fu.jogo[l][c] == " ":                                   #Espaços vazios não devem ser deletados
            alerta = "Nao se pode excluir uma posicao vazia!"
        else:
            fu.jogo[l][c] = " "                                    # Excluindo o valor caso aquelas condicoes tenham sido atendidas
            alerta = "Valor excluido!"
    elif entrada[2] == '?': # Para saber as possibilidades daquela posicao
        alerta = fu.dica(c, l)
    else:                   # Para adiconar um valor ao jogo
        if not fu.pista[l][c]: #falta uma função para dizer se o valor pode ou não
            if fu.jogo[l][c] != " ":
                certeza = input("Voce deseja substituir o valor atual? [S/N] ")
                certeza = certeza.upper()
                if certeza == "S":
                    fu.jogo[l][c] = entrada[2]
                    alerta = "Valor alterado!"
            else: 
                fu.jogo[l][c] = entrada[2]
                alerta = "Valor adicionado!"
    fu.tabelaSudoku(alerta)

    

                                                                                           