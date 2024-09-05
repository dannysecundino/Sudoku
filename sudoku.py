import functions as fu                      # Estamos importando as funções do arquivo "functions.py"
import sys                                  # Importando a biblioteca para 
arquivos = sys.argv                         # Esta lendo as informações dadas no terminal
arquivo = open(arquivos[1], "r")            # Esta abrindo o arquivo com o nome dado no terminal
linhas = arquivo.readlines()        
for coordenadas in linhas:                  #Estamos percorrendo todas as linhas do arquivo aberto

#teste    

#acao = str(input("\n            Digite sua entrada:"))                                                                                            