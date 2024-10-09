cidades = ["Brasília", "Rio de Janeiro", "São Paulo", "Salvador", "Fortaleza"]

quantidade=0

resposta=str(input("Digite a cidade que você quer saber: "))

resposta="".join(resposta.split())

resposta=resposta.lower()

if resposta=="riodejaneiro":
    resposta=cidades[1]
    
elif resposta=="brasília" or resposta=="brasilia":
    resposta=cidades[0]

elif resposta=="saopaulo" or resposta=="sãopaulo":
    resposta=cidades[2]
    
elif resposta=="salvador":
    resposta=cidades[3]
    
elif resposta=="fortaleza":
    resposta=cidades[4]

for cidade in cidades:
    if resposta==cidade:
        quantidade+=1

if quantidade==1:
    print(f"A sua cidade: {resposta} foi encontrada")
else:
    print(f"A sua cidade: {resposta} não foi encontrada")