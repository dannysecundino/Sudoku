import functions as fu                      # Estamos importando as funções do arquivo "functions.py"
import sys                                  # Importando a biblioteca para 



# Recebendo arquivo
arquivos = sys.argv                         # Esta lendo as informações dadas no terminal
arquivo = open(arquivos[1], "r")            # Esta abrindo o arquivo com o nome dado no terminal
linhas = arquivo.readlines()        
for coordenadas in linhas:                  # Estamos percorrendo todas as linhas do arquivo aberto
    if coordenadas != "":                   # Testando se a linha nao estah vazia
        coordenadas = fu.formata(coordenadas)   # Transformando as coordenadas em uma lista
        fu.setPista(coordenadas[1], coordenadas[0], coordenadas[2]) # Adicionando as pistas na matriz principal do jogo
fu.tabelaSudoku("")                           # A tabela ja sera printada com as pistas
  


# Agora o jogo comeca de fato
while not fu.tabelaCompletada(): # Esse laco vai se repetir enquanto a tabela nao estiver completa

    #Recebendo uma entrada
    entrada = input("   Digite a sua entrada: ")
    entrada = fu.formata(entrada)   # Tratando a entrada dada
    l = entrada[1]                  # Pegando a linha
    c = entrada[0]                  #   Pegando a coluna

    alerta = fu.acaoDoUsuario(l, c, entrada[2])

    # Printando a nova tabela apos as alteracoes da jogada
    fu.tabelaSudoku(alerta)

#PROVISORIO: saindo do laco
print("O JOGO ACABOU!!!")                 