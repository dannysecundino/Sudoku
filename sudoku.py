import functions as fu                      # Estamos importando as funções do arquivo "functions.py"
import sys                                  # Importando a biblioteca para 
arquivos = sys.argv                         # Esta lendo as informações dadas no terminal
arquivo = open(arquivos[1], "r")            # Esta abrindo o arquivo com o nome dado no terminal
linhas = arquivo.readlines()        
for coordenadas in linhas:                  # Estamos percorrendo todas as linhas do arquivo aberto
    coordenadas = fu.formata(coordenadas)   # Transformando as coordenadas em uma lista
    fu.setPista(coordenadas[1], coordenadas[0], coordenadas[2]) # Adicionando as pistas na matriz principal do jogo
fu.tabelaSudoku("")                           # A tabela ja sera printada com as pistas
  

while not fu.tabelaCompletada(): # Esse laco vai se repetir enquanto a tabela nao estiver completa

    #Recebendo uma entrada
    entrada = input("   Digite a sua entrada: ")
    entrada = fu.formata(entrada)   # Trantando a entrada dada
    l = entrada[1]                  # Pegando a linha
    c = entrada[0]                  #   Pegando a coluna



    # Agora vamos trabalhar com o que recebemos do input() e que foi tratado pela funcao formata()

    # Para excluir uma posicao
    if entrada[2] == '!':                                              
        if fu.pista[l][c]:                                             # Pistas nao podem ser excluidas
            alerta = "Nao se pode excluir uma pista!"
        elif fu.jogo[l][c] == " ":                                     # Espaços vazios não devem ser deletados
            alerta = "Nao se pode excluir uma posicao vazia!"
        else:                                                          # Excluindo o valor caso aquelas condicoes tenham sido atendidas
            fu.jogo[l][c] = " "                                        
            alerta = "Valor excluido!"


    # Para saber as possibilidades daquela posicao
    elif entrada[2] == '?':                                            
        alerta = f"Possibilidades: {fu.dica(l,c)}"


    # Para adiconar um valor ao jogo
    else:          
        if fu.podeSerAdicionado(l, c, entrada[2]):  # O valor soh pode ser adicionado se ele estiver na lista de dicas

            if not fu.pista[l][c]:  # Uma pista nao pode ser substituída

                if fu.jogo[l][c] != " ":    # Sobrescrever o valor 

                    certeza = input("Voce deseja substituir o valor atual? [S/N] ")
                    certeza = certeza.upper()
                    if certeza == "S":    # Garantir que o usuario quer sobrescrever o valor
                        fu.jogo[l][c] = entrada[2]
                        alerta = "Valor alterado!"
                    else:                 # Caso o usuario nao queira sobrescrever o valor
                        alerta = "Jogue novamente!"

                else:                       # Adicionar Valor
                    fu.jogo[l][c] = entrada[2]
                    alerta = "Valor adicionado!"

            else:   # Uma pista nao pode ser substituída                         
                alerta = "Voce nao pode sobrescrever uma pista!"

        else:   # O valor soh pode ser adicionado se ele estiver na lista de dicas
            alerta = "Esse valor nao pode ser adicionado!"


    # Printando a nova tabela apos as alteracoes da jogada
    fu.tabelaSudoku(alerta)



    

                                                                                           