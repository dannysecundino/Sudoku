import functions as fu                      # Estamos importando as funções do arquivo "functions.py"
import sys                                  # Importando a biblioteca para 
arquivos = sys.argv                         # Esta lendo as informações dadas no terminal
arquivo = open(arquivos[1], "r")            # Esta abrindo o arquivo com o nome dado no terminal
linhas = arquivo.readlines()        
for coordenadas in linhas:                  # Estamos percorrendo todas as linhas do arquivo aberto
    coordenadas = fu.formata(coordenadas)   # Transformando as coordenadas em uma lista
    fu.setPista(coordenadas[1], coordenadas[0], coordenadas[2]) # Adicionando as pistas na matriz principal do jogo
fu.tabelaSudoku()                           # A tabela ja sera printada com as pistas
  

while True:     #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Provisorio!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    entrada = input()
    entrada = fu.formata(entrada)
    #print(entrada)
    l = entrada[1]
    c = entrada[0]
    if entrada[2] == '!':
        fu.excluir(l, c)
    elif entrada[2] == '?':
        print(fu.dica(c, l))
    else:
        if not fu.pista[l][c]: #falta uma função para dizer se o valor pode ou não
            fu.jogo[l][c] = entrada[2]
    fu.tabelaSudoku()

    

#acao = str(input("\n            Digite sua entrada:"))                                                                                            