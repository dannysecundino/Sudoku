import functions as fu                                             # Para melhorar a visibilidade do codigo, separamos a funcao do main



fu.tabelaSudoku()


acao = str(input("\n            Digite sua entrada:"))                                                 # Como o usuario eh burro, nos precisamos remover todos os " ", "," e ":"                                           
acao = fu.formata(acao)                             
if acao[0] == "!" and not fu.pista[acao[2]][acao[1]]:
    fu.jogo[acao[2]][acao[1]] = " "
#elif acao[0] == "?":
    #todo: printar todas as possibilidades da linha/coluna/tabela3x3

fu.tabelaSudoku() 
