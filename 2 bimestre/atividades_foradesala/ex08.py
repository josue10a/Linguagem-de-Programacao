nomes = ["Ana", "Pedro", "Ana", "João", "Pedro", "Maria"]

i=[]

for nome in nomes:
    if nome not in i:
        i.append(nome)
        
print(i)

#1