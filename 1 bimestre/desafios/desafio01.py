a=float(input("Digite o primeiro número: "))
b=float(input("Digite o segundo número: "))
c=float(input("Digite o terceiro número: "))

def ler_numeros():
    print(f'Os números lidos são: {a}, {b} e {c}')

ler_numeros()

def calcular_soma():
    somar=a+b+c
    
    print(f'A soma é: {somar}')
    
calcular_soma()

def calcular_media():
    media=(a+b+c)/3
    
    print(f'A média é: {media}')
    
calcular_media()