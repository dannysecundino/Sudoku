s = s.replace(","," ")      # Trocamos todos "," por " "
s = "adasd dsad"
s = s.replace(":"," ")      # Trocamos todos ":" por " "
x = s.replace(" ","") 
y = list(x.split()) 
s = list(s.split())
print(len(x))
print(len(s))
print(len(y))
print(y)
print(x)
print(s)


 # Assim, uma string que seria "!A,2: 9" se transforma em "!A 2  9"
    s = list(s.split())         # A agora basta dar um split e criar uma lista com todas as informacoes != de " "
    #                           # retornando ['!A' , '2', '']