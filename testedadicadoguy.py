import functions as fu

matriz1x1 = [[" ", " ", " "],
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

def dica(c,l):
    valores_possiveis = [1,2,3,4,5,6,7,8,9]
    for i in range (9): #conferir a linha, coluna e 3x3s
        for j in range (1,10):
            if (fu.jogo[c][i] == j) or (fu.jogo[i][l] == j):
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
            