#exercicio1

def nome(n):
    return f"Nome: {n}"
print(nome(input("Digite o nome:")))

#exercicio2

def soma(n1,n2):
    return n1+n2
print("Soma: ", soma(int(input("Primeiro número: ")), int(input("Segundo número: "))))


#exercicio3
fruits=["maca", "banana", "laranja"]
for i, fruta in enumerate(fruits):
    if i==1:
        print(fruta)
#exercicio4

lista=["mamao", "maça", "banana"]
lista.append("uva")
print(lista)
lista.remove("mamao")
print(lista)

#exercicio5

numeros=[10,10,10,10,10]
print(sum(numeros))