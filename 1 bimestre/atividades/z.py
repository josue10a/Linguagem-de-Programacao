x=int(10)

print(x)


lista=[0,1]
lista.append(2)

print(lista)

lista.append(3)

print(lista)

lista.pop(-1)
print(lista)

y=10
z=5
d=y/z
print(d)

a=5
b=10
print(a+b)

c="123"

print(int(123))

ze=10
ze=ze-7
print(ze)

ze1=10**2
print(ze1)

ze2=20//3
print(ze2)

ze3=10
ze3+=5
print(ze3)

ze4=10
ze4=10+5
print(ze4)

numero = int(input("Digite um número inteiro: "))
if numero%2==0:
       print("O número é par.")
else:    
       print("O número é ímpar.")
       

def verifica_par(numero):
    if numero%2==0:
       return "Par"
    else:    
       return "Ímpar"
   
print(verifica_par(int(input("Digite seu número: "))))

def maior_numero(numero1,numero2):
    if numero1>numero2:
        return f"{numero1} > {numero2}"
    
    elif numero2>numero1:
        return f"{numero2} > {numero1}"
    else:
        return f"Número iguais"


print(maior_numero(float(input("Digite seu primeiro número: ")), float(input("Digite seu segundo número: "))))

def verifica_positivo_negativo(numero):
    if numero>0:
        return "Positivo"
    elif numero<0:
        return "Negativo"
    else:
        return "Zero"
    
print(verifica_positivo_negativo(float(input("Digite um número: "))))

def e_maior_idade(idade):
    if idade>=18:
        return "Maior de idade"
    else:
        return "Menor de idade"
    
print(e_maior_idade(int(input("Digite a idade: "))))

def nota_final(media):
    if media>=7:
        return "Aprovado"
    elif media<=6.9 and media>=5:
        return "Recuperação"
    else:
        return "Reprovado"
    
print(nota_final(float(input("Digite a média: "))))

def calcula_imposto(salario, dependentes):
    salario1=salario-2000
    salario2=salario1*0.15
    salario2+=salario2
    salario3=salario-4000
    salario4=salario3*0.275
    salario4+=salario4
    dependentes1=dependentes*200
    
    if salario<2000:
        return f"Valor do Imposto: 0. Dedução: {dependentes1}"
    elif salario<=4000:
        return f"Valor do Imposto: {salario2}. Dedução: {dependentes1}"
    else:
        return f"Valor do Imposto: {salario4}. Dedução: {dependentes1}"
    
print(calcula_imposto(float(input("Digite o valor do salário: ")), int(input("Digite a quantidade de dependentes: "))))

def classificar_triangulo(lado1, lado2, lado3):
    if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
        if lado1 == lado2 == lado3:
            return "Equilátero"
        elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
            return "Isósceles"
        else:
            return "Escaleno"
    else:
        return "Valores não formam um triângulo"
    
print(classificar_triangulo(float(input("Digite o primeiro lado: ")), float(input("Digite o segundo lado: ")), float(input("Digite o terceiro lado: "))))