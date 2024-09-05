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

    print("<<<=======================SUDOKU DA FuP=======================>>>")  #Cabecalho
    print("")

    
    print("    A   B   C    D   E   F    G   H   I")                # Iniciando a visualizacao do sudoku
    for i in range(9):                                              # Vai percorrer as 9 linhas (0,9]
        if i == 3 or i == 6:                                        # Nas linhas apos o a linha "3" e a linha "6" o padrao de linha muda de "+" e "-" para "+" e "="
            print(" ++===+===+===++===+===+===++===+===+===++ ")    # Linhas com "+" e "="
        else:                                                       
            print(" ++---+---+---++---+---+---++---+---+---++ ")    # Linhas mais comuns
        print(f"{i+1}|| {jogo[i][0]} | {jogo[i][1]} | {jogo[i][2]} || {jogo[i][3]} | {jogo[i][4]} | {jogo[i][5]} || {jogo[i][6]} | {jogo[i][7]} | {jogo[i][8]} ||{i+1}")
    print(" ++---+---+---++---+---+---++---+---+---++ ")            
    print("    A   B   C    D   E   F    G   H   I")                # Finalizacao da visualizacao do sudoku

    #Faremos, agora o menu de entradas
    print("")
    print("")
    print("                >>>MENU<<<                ")
    print("=>   Adcionar Pistas: &<Coluna>,<Linha>: <Valor>")  #PROVISORIO!!!
    print("=>   Realizar Jogada: <Coluna>,<Linha>: <Valor>")
    print("=>   Excluir Valor: !<Coluna>,<Linha>")
    print("=>   Conferir Possibilidades: ?<Coluna>,<Linha>")



def letraParaNumero(letra: str):                                         # Funcao para tranformar os inputs de letras para numeros (que serao usados na manipulacao das colunas das matrizes)
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
      
def setPista(l: int, c: int, valor:int):                                          # Estamos demarcando que a coordenada eh ou nao uma pista (pois elas sao inalteradas e indeletaveis)
    jogo[l-1][c] = valor                                            # A linha eh "-1", pois o usario vai colocar uma entrade entre [1,9] e o programa vai trabalhar com numeros de [0,8]
    pista[l-1][c] = True
    

tabelaSudoku()

acao = str(input())                                                 # Como o usuario eh burro, nos precisamos remover todos os " ", "," e ":"                     
acao = acao.replace(" ","")                                         # A forma que utilizamos foi usando a funcao replace que troca um elemento qualquer da string por outro
acao = acao.replace(",","")                                         # Trocamos " ", "," e ":" por "" (nulo)
acao = acao.replace(":","")
acao = list(acao)                                               
acao[2], acao[3] = int(acao[2]), int(acao[3])                       # Transformar a linha e o numero em inteiros (era string)
acao[1] = letraParaNumero(acao[1])                                  # Transforma a letra da coluna no seu numero correspondente
if acao[0] == "&":                                                  # Provisório para adicionar pistas
    setPista(acao[2],acao[1],acao[3])
else:
    if pista[acao[2],acao,[1]]:
        print("ameiii🧓")

tabelaSudoku() 
