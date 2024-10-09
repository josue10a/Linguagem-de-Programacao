carros=["golf", "corolla", "mustang", "bmw-serie3", "civic"]

carros.append("Rolls Royce")
carros.remove("civic")

print(carros)

carros.insert(0, "MAMAE")

print(carros)

def contador(a):
    return f"O número de caractere que tem: {len(a)}"
     
print(contador(input("Digite os caracteres: ")))

