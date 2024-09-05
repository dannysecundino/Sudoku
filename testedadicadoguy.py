import sys

arquivos = sys.argv
arquivo = open(arquivos[1], "r")
linhas = arquivo.readlines()
for coordenadas in linhas:
    print(coordenadas)