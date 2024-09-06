import functions as fu                      # Estamos importando as funções do arquivo "functions.py"
import sys                                  # Importando a biblioteca para 
import os                                   # Estamos utilizando apenas para limpar o terminal




# Recebendo arquivo
arquivos = sys.argv                         # Esta lendo as informações dadas no terminal
arquivo = open(arquivos[1], "r")            # Esta abrindo o arquivo com o nome dado no terminal
linhas = arquivo.readlines()  

erroTabela = False  # Ira retornar o erro de ferimento das regras do jogo nas pistas caso ele ocorra
erroNumeroDePistas = False  # Ira retornar o erro de numero de pistas fora do intervalo [1,80] caso ele ocorra
numeroDePistas = 0  # Contralara o numero de pistas
errosDeFormatacaoPistas = 0

for coordenadas in linhas:                  # Estamos percorrendo todas as linhas do arquivo aberto
    if coordenadas != "":                   # Testando se a linha nao estah vazia
        coordenadas = fu.formata(coordenadas)   # Transformando as coordenadas em uma lista

        l = coordenadas[1]
        c = coordenadas[0]
        valor = coordenadas[2]
        
        if l != "erro" and c != "erro" and valor != "erro":
            if fu.podeSerAdicionado(l,c,valor):
                fu.setPista(l,c,valor) # Adicionando as pistas na matriz principal do jogo
                numeroDePistas += 1
            else:
                erroTabela = True
        else:
            errosDeFormatacaoPistas += 1
        
alerta = f"Houveram {errosDeFormatacaoPistas} pistas declaradas com erros de formatacao!"

if numeroDePistas < 1 or numeroDePistas > 80:
    erroNumeroDePistas = True
            














if not erroTabela and not erroNumeroDePistas:   # Caso não haja erros na captacao de pistas
    fu.tabelaSudoku(alerta)                           # A tabela ja sera printada com as pistas

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

else:   # Caso haja algum erro na captacao de pistas (erro de regras ou erro de numro de pistas)
    os.system("cls")

    print(alerta)

    print("=====>>ERROR<<=====")
    
    # Usaremos dois if's, porque, caso ocorra de os dois erros acontecerem, isso deve ser informado para o usuario
    if erroTabela:
        print("As pistas fornecidas feriram as regras do jogo.")
    if erroNumeroDePistas:
        print("O numero de pistas fornecidas estah fora do intervalo [1,80].") 
    
    print("Tente Novamente!")        