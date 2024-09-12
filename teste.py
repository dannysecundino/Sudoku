s = "adasd dsad"
s = s.replace(","," ")      # Trocamos todos "," por " "
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
