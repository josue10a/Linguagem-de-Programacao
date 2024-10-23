import copy

#Questão 1:

def n(n1):
    
    if n1>0:
      if n1%2==0:
          return f"O número {n1} é par"
      else:
          return f"O número {n1} é ímpar"  
    elif n1<0:
      return f"O número {n1} é negativo"
    else:
      return f"O número {n1} é igual a 0"        

print(n(int(input("Digite o número: "))))


#Questão 2:

def ni(nu, nd, nt):
    
    if (nu>nd) and (nu>nt):
        
        return f"Maior número: {nu}"
    
    elif (nd>nu) and (nd>nt):
        
        return f"Maior número: {nd}"
    
    elif (nt>nu) and (nt>nd):
        
        return f"Maior número {nt}"
    
    else:
        
        return f"{nu} igual a {nd} e {nt}"
    
print(ni(int(input("\n \nDigite o primeiro número: ")), int((input("Digite o segundo número: "))), int(input("Digite o terceiro número: "))))
 
 
#Questão 3:

def m(np, ns, nte):
    
    media=(np+ns+nte)/3
    
    if media<60:
        
        return f"Reprovado, nota: {media}"
    
    elif media>70:
        
        return f"Aprovado com distinção, nota: {media}"
    
    else:
        
        return f"Aprovado, nota: {media}"
    
print(m(float(input("\n \nDigite a primeira nota: ")), float(input("Digite a segunda nota: ")) , float(input("Digite a terceira nota: "))))

#Questão 4:

def id(i):
    
    if i<12:
        return f"Criança"
    elif i>=12 and i<=17:
        return f"Adolescente"
    elif i>=18 and i<=64:
        return f"Adulto"
    else:
        return f"Idoso"
    
print(id(float(input("\n \nDigite a idade: "))))

#Questão 5:

def numero(nume):
    
    if nume%2==0 and nume%3==0:
        return f"Divisivel por 2 e 3: {nume}"
    elif nume%3==0:
        return f"Divisivel por 3: {nume}"
    elif nume%2==0:
        return f"Divisivel por 2: {nume}"
    else:
        return f"Seu número {nume} não é divisel por 2 e nem por 3"
    
print(numero(float(input("\n \nDigite seu número: "))))


#Questão 6:

def list():
    
    lista_original=[1,2,3,4,5]
    
    lista_copia=lista_original.copy()
    
    lista_copia[0]=10
    
    print(f"Lista original: {lista_original} \nLista copia: {lista_copia}")
    
list()

#Questão 7:

def codigo(no1, no2, no3, no4, no5):
    
    lista1=[no1, no2, no3, no4, no5]
    
    lista2=lista1[:]
    
    print(f"\nLista original: {lista1} \nLista copia{lista2}")
    
    lista2[0]="Nome Alterado"
    
    print(f"\nProva que são listas independentes: Lista original: {lista1} \nLista copia{lista2} ")
    
codigo(str(input("\n \nDigite o primeiro nome: ")), str(input("Digite o segundo nome: ")), str(input("Digite o terceiro nome: ")), str(input("Digite o quarto nome: ")), str(input("Digite o quinto nome: ")))

#Questão 8:

def list1():
    
    numeros=[10, 20, 30, 40]
    
    numeros_clone=numeros.copy()
    
    numeros_clone[3]=99
    
    return f"\n \nLista original: {numeros}, Lista clone: {numeros_clone}"

print(list1())
    
#Questão 9:

#Usando o metodo de atribuição(=) a lista original e a lista copia vao apontar para o mesmo local de memória. Sendo que, a lista copia se torna referência da outra. Desse modo, quando alteramos um valor da lista original ou lista copia as duas vão ser alteradas. Exemplo:

listaoriginal1=[1,2]

listacopia1=listaoriginal1

print(f"\n \nLista original: {listaoriginal1}, Lista copia: {listacopia1}")

listacopia1.append(3)

print(f"\n \nModificação na lista copia. Lista original: {listaoriginal1}, Lista copia: {listacopia1}")

#Usando o metodo de copy() ou fatiamento([:]) vai ser criado uma lista copia igual a lista original, entretanto em um local diferente da memória, fazendo desse modo com que alterações na lista original ou lista copia não se afetem. Exemplo:

#Metodo de copy():

listaoriginal2=[4,5,6]

listacopia2=listaoriginal2.copy()

print(f"\n \nLista original: {listaoriginal2}, Lista copia: {listacopia2}")

listacopia2.append(7)

print(f"\n \nModificação na lista copia. Lista original: {listaoriginal2}, Lista copia: {listacopia2}")

#Metodo de fatiamento([:])

listaoriginal3=[8,9,10]

listacopia3=listaoriginal3[:]

print(f"\n \nLista original: {listaoriginal3}, Lista copia: {listacopia3}")

listacopia3.append(11)

print(f"\n \nModificação na lista copia. Lista original: {listaoriginal3}, Lista copia: {listacopia3}")

#Questão 10:

itens=["maçã", "banana", "laranja"]

itens1=copy.deepcopy(itens)

print(f"\n \nLista original: {itens}, Lista copia: {itens1}")

itens1.append("uva")

print(f"\n \nModificação na lista copia. Lista original: {itens}, Lista copia: {itens1}")