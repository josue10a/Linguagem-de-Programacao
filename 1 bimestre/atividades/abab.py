import math
def banco():
    pre=[]
    clientes = []
    numero = 1
    
    while True:
        
        pergunta1=input("Fila preferencial ou normal? se quiser parar digite pare: ").strip().lower()
    
        if pergunta1=="normal":
            clientes.append(numero)
            print(f'Seu número da fila: {numero}')
            numero += 1
        
        elif pergunta1=="preferencial":
    
            pre.append(numero)
            print(f'Seu número da fila: {numero}')
            numero += 1
        
        elif pergunta1=="pare":
            break
        
        else:
            print("Preferencial ou normal")
            
    pre.sort()
    clientes.sort()
    return f"Fila normal: {clientes}",f"Fila preferencial: {pre}"

# Chama a função e imprime o resultado
print(banco())


#do professor:

def fila_banco(fila_clientes):
    while fila_clientes:
        proximo_atendido=fila_clientes[0]
        fila_clientes.remove(proximo_atendido)
        print(f"Próximo cliente: {proximo_atendido}")
        print(f"Restam na fila: {fila_clientes}")
    
    
fila_banco(["Jõao","Maria"])


def par_ou_impar():
    n=float(input(f"Digite um número: "))
    n1=round(n,0)
    if n1%2==0:
        print("par")
    else:
        print("ímpar")
        
par_ou_impar()

    
    

    
