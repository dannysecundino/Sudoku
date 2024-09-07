import functions as fu                         # Estamos importando as funções do arquivo "functions.py"
import sys                                     # Importando a biblioteca para pegar o arquivo
import os                                      # Estamos utilizando apenas para limpar o terminal

# Recebendo arquivo
arquivos = sys.argv                             # Esta lendo as informações dadas no terminal
arquivo = open(arquivos[1], "r")                # Esta abrindo o arquivo com o nome dado no terminal
linhas = arquivo.readlines()  

erroTabela = False                              # Ira retornar o erro de ferimento das regras do jogo nas pistas caso ele ocorra
erroNumeroDePistas = False                      # Ira retornar o erro de numero de pistas fora do intervalo [1,80] caso ele ocorra
numeroDePistas = 0                              # Controlara o numero de pistas
errosDeFormatacaoPistas = 0
qualFoiQueDeuErro = []

for coordenadas in linhas:                      # Estamos percorrendo todas as linhas do arquivo aberto
    if coordenadas != "":                       # Testando se a linha nao estah vazia
        coordenadas = fu.formata(coordenadas)   # Transformando as coordenadas em uma lista

        l = coordenadas[1]
        c = coordenadas[0]
        valor = coordenadas[2]
        tamanhoDaPista = len(coordenadas)       
        
        if (l != "erro") and (c != "erro") and (valor != "erro"):   # Conferindo se ha erros na pista (letras fora de A a I ou Numeros fora do intervalo [1,9])

            if fu.podeSerAdicionado(l,c,valor):
                fu.setPista(l,c,valor)                              # Adicionando as pistas na matriz principal do jogo
                numeroDePistas += 1
            else:
                erroTabela = True

        else:
           errosDeFormatacaoPistas += 1
           qualFoiQueDeuErro.append(f"{coordenadas[0]},{coordenadas[1],coordenadas[2]}")

alerta = f"Houveram {errosDeFormatacaoPistas} pistas declaradas de forma invalida!"

if numeroDePistas < 1 or numeroDePistas > 80:
    erroNumeroDePistas = True
            














if not erroTabela and not erroNumeroDePistas:   # Caso não haja erros na captacao de pistas
    fu.tabelaSudoku(alerta)                     # A tabela ja sera printada com as pistas

    # Agora o jogo comeca de fato
    while not fu.tabelaCompletada():            # Esse laco vai se repetir enquanto a tabela nao estiver completa

        #Recebendo uma entrada
        entrada = input("   Digite a sua entrada: ")
        entrada = fu.formata(entrada)           # Tratando a entrada dada
        l = entrada[1]                          # Pegando a linha
        c = entrada[0]                          # Pegando a coluna
        tamanhoDaEntrada = len(entrada)


        if (l != "erro") and (c != "erro") and (entrada[2] != "erro") and (tamanhoDaEntrada == 3):  # Conferindo se ha erros na entrada (letras fora de A a I ou Numeros fora do intervalo [1,9])
            alerta = fu.acaoDoUsuario(l, c, entrada[2])
        
        else:
            alerta = "Entrada invalida! Tente Novamente!"

        # Printando a nova tabela apos as alteracoes da jogada e com o alerta correspondente
        fu.tabelaSudoku(alerta)

    #PROVISORIO: saindo do laco
    fu.fimDeJogo()

else:   # Caso haja algum erro na captacao de pistas (erro de regras ou erro de numro de pistas)
    fu.errorPistas(erroTabela,erroNumeroDePistas,alerta)