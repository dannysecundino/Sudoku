import os                                                           # Estamos utilizando apenas para limpar o terminal

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
    
def tabelaSudoku(alerta):                                                 # Visualizacao do sudoku e do menu
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
    print(f"        {alerta}")

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

def excluir(l,c):
    if pista[l][c] and jogo[l][c] != " ":                                             # Pistas nao podem seer excluidas
        jogo[l][c] = " "                                    # Excluindo o valor caso aquelas condicoes tenham sido atendidas

def testesRestentes(l,c):   # Essa funcao nos ajudara na funcao dica(), ja que ela ira dar dar o restante de testes necessarios de acordo com a a posicao relativa na matriz 3x3 em que a linha e a coluna correspondente estao incicando
    p = str(l) + str(c)         # Para facilitar os testes, usaremos a concatenacao das stirngs dos valores dados como parametros


    if p == "00" or p == "03" or p == "06" or p == "30" or p == "33" or p == "36" or p == "60" or p == "63" or p == "66":
        testes_restantes = [jogo[l+1][c+1], jogo[l+2][c+1], jogo[l+1][c+2], jogo[l+2][c+2]]
    
    elif p == "01" or p == "04" or p == "07" or p == "31" or p == "34" or p == "37" or p == "61" or p == "64" or p == "67":
        testes_restantes = [jogo[l+1][c-1], jogo[l+1][c+1], jogo[l+2][c-1], jogo[l+2][c+1]]

    elif p == "02" or p == "05" or p == "08" or p == "32" or p == "35" or p == "38" or p == "62" or p == "65" or p == "68":
        testes_restantes = [jogo[l+1][c-1], jogo[l+2][c-1], jogo[l+1][c-2], jogo[l+2][c-2]]

    elif p == "10" or p == "13" or p == "16" or p == "40" or p == "43" or p == "46" or p == "70" or p == "73" or p == "76":
        testes_restantes = [jogo[l-1][c+1], jogo[l-1][c+2], jogo[l+1][c+1], jogo[l+1][c+2]]

    elif p == "11" or p == "14" or p == "17" or p == "41" or p == "44" or p == "47" or p == "71" or p == "74" or p == "77":
        testes_restantes = [jogo[l-1][c-1], jogo[l-1][c-1], jogo[l+1][c-1], jogo[l+1][c+1]]
    
    elif p == "12" or p == "15" or p == "18" or p == "42" or p == "45" or p == "48" or p == "72" or p == "75" or p == "78":
        testes_restantes = [jogo[l-1][c-2], jogo[l-1][c-1], jogo[l+1][c-2], jogo[l+1][c-1]]

    elif p == "20" or p == "23" or p == "26" or p == "50" or p == "53" or p == "56" or p == "80" or p == "83" or p == "86":
        testes_restantes = [jogo[l-1][c+1], jogo[l-2][c+1], jogo[l-1][c+2], jogo[l-2][c+2]]

    elif p == "21" or p == "24" or p == "27" or p == "51" or p == "54" or p == "57" or p == "81" or p == "84" or p == "87":
        testes_restantes = [jogo[l-2][c-1], jogo[l-1][c-1], jogo[l-2][c+1], jogo[l-1][c+1]]
    
    elif p == "22" or p == "25" or p == "28" or p == "52" or p == "55" or p == "58" or p == "82" or p == "85" or p == "88":
        testes_restantes = [jogo[l-2][c-2], jogo[l-1][c-2], jogo[l-2][c-1], jogo[l-1][c-1]]

    return testes_restantes

def dica(l,c):
    
    # Vamos partir da suposicao de que todos os valores estao disponiveis ate que se prove o contrario
    valores_possiveis = ["1","2","3","4","5","6","7","8","9"]
    nao_pode = []                           # Vamos adicionar os valores que nao sao possiveis qui para depois retira-los


    # Conferindo a linha e a coluna
    for i in range(9):
        if i != l:  # Conferindo a coluna
            if jogo[i][c] != " ":
                nao_pode.append(jogo[i][c])
        if i != c:  # Conferinndo a linha
            if jogo[l][i] != " ":
                nao_pode.append(jogo[l][i])

    # Conferindo (o restante) da matriz 3x3 na qual a posicao se encontra
    resto = testesRestentes(l,c)

    for item in resto:
        if item != " ":
            nao_pode.append(item)

    # Agora a lista nao_pode tem todos os valores impossiveis

    valores_possiveis = set(valores_possiveis) - set(nao_pode)  # Transformamos as listas em conjuntos para podermos subtrair um do outro
    valores_possiveis = list(valores_possiveis)


    return valores_possiveis

def tabelaCompletada():
    completo = True
    for i in range(9):
        for j in range(9):
            if jogo[i][j] == " ":
                completo = False
    
    return completo

def podeSerAdicionado(l,c, valor):  # Nos dira se a jogada eh valida ou nao
    possiveis = dica(l,c)

    pode = False    # Parte-se do principio de que o valor nao eh possivel

    for item in possiveis:
        if item == valor:   # Se o valor for igual a algum dos valores possiveis, entao a funcao retornara que pode ser adicionado (True)
            pode = True

    
    return pode
