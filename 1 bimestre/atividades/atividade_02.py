nome,idade="Josué ",18

print(nome,idade)


#transformação em: 
#strings: str()
#decimal: float()
#inteiro: int()

n1=10
n2=20

r=n1+n2

print(r)

def estoque():
 product_name="Camiseta"

 product_price=29.99

 stock_quantity=50

 print(f' Produto: {product_name} \n Preço do Produto: {product_price} \n Quantidade de estoque: {stock_quantity}')
 
estoque()

def venda_produto(stock_quantity, quantidadevendida):
    stock_quantity= stock_quantity- quantidadevendida
    
    print(f'Quantidade de estoque: {stock_quantity}')
    
venda_produto(30, 4)


def cadastro():
    nome=str(input("Digite seu nome: "))
    sobrenome= str(input("Digite seu sobrenome: "))
    idade=int(input("Digite a idade: "))
    
    if not isinstance(nome, sobrenome, str) and not isinstance(idade, int):
        print("Error")
    else:
        print(f' Nome: {nome}\n Sobrenome: {sobrenome}\n Idade: {idade}')
        
cadastro()

 
