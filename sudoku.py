import functions as fu                         # Estamos importando as funcoes que fizemos do arquivo "functions.py"
import sys                                     # Importando a biblioteca para pegar o arquivo


# Recebendo arquivo
arquivos = sys.argv                             # Esta lendo as informações dadas no terminal
quantidadeDeArquivos = len(arquivos)            # Arquivo sudoku.py + arquivos de entrada



if quantidadeDeArquivos == 2:                   # Modo INTERATIVO

    arquivo = open(arquivos[1], "r")                # Esta abrindo o arquivo com o nome dado no terminal
    linhas = arquivo.readlines()  

    erroTabela = False                              # Ira retornar o erro de ferimento das regras do jogo nas pistas caso ele ocorra
    erroNumeroDePistas = False                      # Ira retornar o erro de numero de pistas fora do intervalo [1,80] caso ele ocorra
    numeroDePistas = 0                              # Controlara o numero de pistas
    errosDeFormatacaoPistas = 0

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

    alerta = f"Houveram {errosDeFormatacaoPistas} pistas declaradas de forma invalida!\n(Isto eh, Colunas com letras apos I, ou Linhas fora de [1,9], ou Pistas fora de [1,9])"

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
                alerta = "Entrada invalida! Tente Novamente!\n(Isto eh, Coluna com letra apos I, ou Linha fora de [1,9], ou Valor fora de [1,9])"

            # Printando a nova tabela apos as alteracoes da jogada e com o alerta correspondente
            fu.tabelaSudoku(alerta)

        # Saindo do laco: Fim de jogo
        fu.fimDeJogo()

    else:   # Caso haja algum erro na captacao de pistas (erro de regras ou erro de numro de pistas)
        fu.errorPistas(erroTabela,erroNumeroDePistas,alerta)





elif quantidadeDeArquivos == 3:                 # Modo BATCH
    arquivoPistas = open(arquivos[1], "r")          # Arquivo contendo as pistas
    linhasPistas = arquivoPistas.readlines()        # Todas as pistas

    arquivoJogadas = open(arquivos[2], "r")         # Arqivo contendo as jogadas
    linhasJogadas = arquivoJogadas.readlines()      # Todas as jogadas


    # Percorreremos todas as linhas do arquivo de pistas aberto 
    i = 0
    erroConfiguracaoDicas = False
    while (not erroConfiguracaoDicas) and (i <= len(linhasPistas) - 1): # Esse laco vai se repetir enquanto nao houver algum erro de configuracao de pistas e a linha que queremos acessar existe no arquivo

        linha = linhasPistas[i]

        if linha != "":                       # Testando se a linha nao estah vazia
            linha = fu.formata(linha)   # Transformando as coordenadas em uma lista
            l = linha[1]
            c = linha[0]
            valor = linha[2]
      
            
            if (fu.jogo[l][c] == " " or fu.jogo[l][c] == valor) and fu.podeSerAdicionado(l,c,valor):   # Conferindo se o espaco que se quer preencher esta vazio ou eh o mesmo valor ja adiconado e se nao fere as regras do jogo

                fu.setPista(l,c,valor)                              # Adicionando as pistas na matriz principal do jogo

            else:                                                                                      # Caso se ponha uma nova dica para a mesma celula ou fira as regras do jogo
                print("Configuracao de dicas invalida.")
                erroConfiguracaoDicas = True


        i += 1


    

    if not erroConfiguracaoDicas:   # O jogo so prossegue se nao hoveram erros de configuracao nas pistas
        jogadasInvalidas = []


        for linha in linhasJogadas:

            # Preparando a possivel mensagem de jogada invalida
            coordenadas = linha.split(": ")
            coordenadas[1] = coordenadas[1].replace("\n","")     # Para evitar que o valor seja printado com a quebra de linha que vem apos ele
            mensagem = f"A jogada ({coordenadas[0]}) = {coordenadas[1]} eh invalida!"   # Mensagem padrao. Caso de erro, sera adicionada na lista jogadas invalidas


            # Fomatando a entrada
            linha = fu.formata(linha)
            l = linha[1]
            c = linha[0]
            valor = linha [2]


            if fu.podeSerAdicionado(l,c,valor) and not fu.pista[l][c]:  # Se nao fere as regras e nao quiser ocupar o lugar de uma pista
                fu.jogo[l][c] = valor                                   # O valor eh adicionado a matriz principal

            else:                                                       # No caso de feriralguma regra ou quiser ocupar o lugar de uma pista
                jogadasInvalidas.append(mensagem)
        # O jogo ja acabou, soh falta apresentar as jogadas invalidas e conferir se a tabela foi completada


        # Printando jogadas invalidas
        for item in jogadasInvalidas:
            print(item)

        # Conferindo se a tabela foi completada
        if fu.tabelaCompletada():                       # Vitoria
            print("A grade foi preenchida com sucesso!")
        else:                                           # Derrota
            print("A grade nao foi preenchida!")





else:                                           # Caso tenham sido informados menos de 2 ou mais de 3 arquivos

    print("ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_\nERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_\nERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_\nERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_\nERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR_ERROR")
    
    print("")
    print("___________________________________________________ORIENTACOES___________________________________________________")
    print("")

    print("MODO INTERATIVO: insira 1 (um) arquivo contendo as pistas do jogo.")
    print("     MODO BATCH: insira 2 (dois) arquivos, um contendo as pistas do jogo e outro contendo as jogadas realizadas.")

    print("_________________________________________________________________________________________________________________")