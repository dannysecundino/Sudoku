import os



jogo = [[" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "]] # Essa "matriz" representara o jogo por completo. Nela, serao adicionadas as pistas e as jogadas do usuario

pista = [[False, False, False, False, False, False, False, False, False],
         [False, False, False, False, False, False, False, False, False],
         [False, False, False, False, False, False, False, False, False],
         [False, False, False, False, False, False, False, False, False],
         [False, False, False, False, False, False, False, False, False],
         [False, False, False, False, False, False, False, False, False],
         [False, False, False, False, False, False, False, False, False],
         [False, False, False, False, False, False, False, False, False],
         [False, False, False, False, False, False, False, False, False]] # Criamos essa matriz para conferir se a coordenada que o jogador tentou fazer alguma ação (deletar ou alterar) é uma pista ou não
    
def tabelaSudoku():
    os.system("cls")#TO DO: em Linux, eh "clear" 

    print("    A   B   C    D   E   F    G   H   I")                #Iniciando a visualização do sudoku
    for i in range(9):                                              #Vai percorrer as 9 linhas (0,9]
        if i == 3 or i == 6:                                        #Nas linhas após o a linha "3" e a linha "6" o padrão de linha muda de "+" e "-" para "+" e "="
            print(" ++===+===+===++===+===+===++===+===+===++ ")    #Linhas com "+" e "="
        else:                                                       
            print(" ++---+---+---++---+---+---++---+---+---++ ")    #Linhas mais comuns
        print(f"{i+1}|| {jogo[i][0]} | {jogo[i][1]} | {jogo[i][2]} || {jogo[i][3]} | {jogo[i][4]} | {jogo[i][5]} || {jogo[i][6]} | {jogo[i][7]} | {jogo[i][8]} ||{i+1}")
    print(" ++---+---+---++---+---+---++---+---+---++ ")            
    print("    A   B   C    D   E   F    G   H   I")                #Finalização da visualização do sudoku


def letraParaNumero(letra): #Funcao para tranformar os inputs de letras para numeros (que serao usados na manipulacao das colunas das matrizes)
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
    
    
def pista(l, c, valor):
    jogo[l][c] = valor
    pista[l][c] = True
    

jogada = list(map(str,input().split()))
jogada = list(jogada[0]).append(jogada[1])

print(jogada)
jogada[1] = letraParaNumero(jogada[1])

if jogada[0] == "&":
    pista(jogada[1], jogada[3], jogada[5])

