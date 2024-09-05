import os                                                           # Estamos utilizando apenas para limpar o output

jogo = [[" ", " ", " ", " ", " ", " ", " ", " ", " "],              # Essa matriz representara o jogo por completo. Nela, serao adicionadas as pistas e as jogadas do usuario
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "]]       

matriz1x1 = [[" ", " ", " "],                                      # Cada matriz 3x3 dentro da grande matriz 81x81
            [" ", " ", " "],
            [" ", " ", " "]]
matriz1x2 = [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]
matriz1x3 = [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]
matriz2x1 = [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]
matriz2x2 = [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]
matriz2x3 = [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]
matriz3x1 = [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]
matriz3x2 = [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]
matriz3x3 = [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]
       

pista = [[False, False, False, False, False, False, False, False, False], # Criamos essa matriz para conferir se a coordenada que o jogador tentou fazer alguma acao (deletar ou alterar) eh uma pista ou nao
         [False, False, False, False, False, False, False, False, False],
         [False, False, False, False, False, False, False, False, False],
         [False, False, False, False, False, False, False, False, False],
         [False, False, False, False, False, False, False, False, False],
         [False, False, False, False, False, False, False, False, False],
         [False, False, False, False, False, False, False, False, False],
         [False, False, False, False, False, False, False, False, False],
         [False, False, False, False, False, False, False, False, False]]
    
def tabelaSudoku():                                                 # Visualizacao do sudoku e do menu
    os.system("cls")                                                # TO DO: em Linux, eh "clear"

    print("<<<==========| SUDOKU DE FuP |==========>>>\n")  #Cabecalho

    
    print("    A   B   C    D   E   F    G   H   I")                # Iniciando a visualizacao do sudoku
    for i in range(9):                                              # Vai percorrer as 9 linhas (0,9)
        if i == 3 or i == 6:                                        # Nas linhas apos o a linha "3" e a linha "6" o padrao de linha muda de "+" e "-" para "+" e "="
            print(" ++===+===+===++===+===+===++===+===+===++ ")    # Linhas com "+" e "="
        else:                                                       
            print(" ++---+---+---++---+---+---++---+---+---++ ")    # Linhas mais comuns
        print(f"{i+1}|| {jogo[i][0]} | {jogo[i][1]} | {jogo[i][2]} || {jogo[i][3]} | {jogo[i][4]} | {jogo[i][5]} || {jogo[i][6]} | {jogo[i][7]} | {jogo[i][8]} ||{i+1}")
    print(" ++---+---+---++---+---+---++---+---+---++ ")            
    print("    A   B   C    D   E   F    G   H   I")                # Finalizacao da visualizacao do sudoku
    print("\n<<<=====================================>>>\n""")

    #Faremos, agora o menu de entradas
    print("        >>>======| MENU |======<<<\n")
    print("-> Realizar Jogada:  <Coluna>,<Linha>: <Valor>")
    print("->   Excluir Valor: !<Coluna>,<Linha>")
    print("->  Possibilidades: ?<Coluna>,<Linha>")
    print("\n         >>>==================<<<")

def letraParaNumero(letra):                                    # Funcao para tranformar os inputs de letras para numeros (que serao usados na manipulacao das colunas das matrizes)
    if letra == "A" or letra == "a":
        return 0
    elif letra == "B" or letra == "b":
        return 1
    elif letra == "C" or letra == "c":
        return 2
    elif letra == "D" or letra == "d":
        return 3
    elif letra == "E" or letra == "e":
        return 4
    elif letra == "F" or letra == "f":
        return 5
    elif letra == "G" or letra == "g":
        return 6
    elif letra == "H" or letra == "h":
        return 7
    elif letra == "I" or letra == "i":
        return 8
      
def setPista(l, c, valor):                            # Estamos demarcando se a coordenada eh ou nao uma pista (pois elas sao inalteradas e indeletaveis)
    jogo[l][c] = valor                                            # A linha eh "-1", pois o usuario vai colocar uma entrada entre [1,9], e o programa vai trabalhar com numeros de [0,8]
    pista[l][c] = True
    
def formata(s):                                               # Como o usuario eh burro, nos precisamos remover todos os " ", "," e ":"; alem disso, vamos formatar outras coisas da entrada para facilitar a manipulação do codigo
    s = s.replace(" ","")                                     # A forma que utilizamos foi usando a funcao replace que troca um elemento qualquer da string por outro
    s = s.replace(",","")                                     # Trocamos " ", "," e ":" por "" (nulo)
    s = s.replace(":","")
    s = list(s)                                               # Tranformamos a string em lista

    if s[0] == "!":
        operacao = s[0]
        s.remove(operacao)
        s.append(operacao)
    elif s[0] == "?":
        operacao = s[0]
        s.remove(operacao)
        s.append(operacao)

    s[0] = letraParaNumero(s[0])
    s[1] = int(s[1]) - 1
    
    return s



def dica(c,l):
    valores_possiveis = [1,2,3,4,5,6,7,8,9]
    for i in range (9): #conferir a linha, coluna e 3x3s
        for j in range (1,10):
            if (jogo[c][i] == j) or (jogo[i][l] == j):
                valores_possiveis.remove(j)
                if c == 0 or c == 1 or c == 2:
                    if l == 0 or l == 1 or l == 2:
                        matriz1x1.remove(j)
                    elif l == 3 or l == 4 or l == 5:
                        matriz1x2.remove(j)
                    else:
                        matriz1x3.remove(j)
                elif c == 3 or c == 4 or c == 5:
                    if l == 0 or l == 1 or l == 2:
                        matriz2x1.remove(j)
                    elif l == 3 or l == 4 or l == 5:
                        matriz2x2.remove(j)
                    else:
                        matriz2x3.remove(j)
                else:
                    if l == 0 or l == 1 or l == 2:
                        matriz3x1.remove(j)
                    elif l == 3 or l == 4 or l == 5:
                        matriz3x2.remove(j)
                    else:
                        matriz3x3.remove(j)
    return valores_possiveis