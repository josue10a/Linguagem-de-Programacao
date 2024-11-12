import tkinter as tk
from tkinter import messagebox

def imc():
    try:
        peso = float(entrada_peso.get())
        altura = float(entrada_altura.get())
        
        imc = peso / (altura ** 2)
        
        #adicionei um cálculo para indicar qual a quantidade de peso que o usuário precisa ganhar(caso esteja abaixo do imc ideal) ou perder(caso esteja acima do imc ideal), para atingir o valor do imc ideal mais próximo, de maneira arredondada, exemplo1(sobrepeso): Um usuário tem o seu imc de 39, ele irá precisar perder x kg para chegar ao imc ideal mais próximo, sendo o 24, de maneira arredondada. exemplo2(abaixo do peso): Um usuário tem o seu imc de 15, ele irá precisar ganhar x kg para chegar ao imc ideal mais próximo, sendo o 19, de maneira arredondada.
        
        #Cálculo sobrepeso:
        peso2=(peso*24)/imc
        peso3=peso-peso2
        
        #Cálculo abaixo do peso:
        peso4=(peso*19)/imc
        peso5=peso4-peso
        
        
        if imc < 18.5:
            classificacao = "Abaixo do peso ideal"
            cor = "blue"
            resultado_texto = f"Seu IMC é: {imc:.2f} \nClassificação: {classificacao} \nVocê precisa ganhar: {peso5:.2f} kg,\npara chegar ao imc 19"
        elif 18.5 <= imc <= 24.9:
            classificacao = "Peso Ideal"
            cor = "green"
            resultado_texto = f"Seu IMC é: {imc:.2f} \nClassificação: {classificacao}"
        elif 25 <= imc <= 29.9:
            classificacao = "Sobrepeso"
            cor = "yellow"
            resultado_texto = f"Seu IMC é: {imc:.2f} \nClassificação: {classificacao} \nVocê precisa perder: {peso3:.2f} kg,\npara chegar ao imc 24"
        elif 30 <= imc <= 34.9:
            classificacao = "Obesidade grau I"
            cor = "orange"
            resultado_texto = f"Seu IMC é: {imc:.2f} \nClassificação: {classificacao} \nVocê precisa perder: {peso3:.2f} kg,\npara chegar ao imc 24"
        elif 35 <= imc <= 39.9:
            classificacao = "Obesidade grau II"
            cor = "red"
            resultado_texto = f"Seu IMC é: {imc:.2f} \nClassificação: {classificacao} \nVocê precisa perder: {peso3:.2f} kg,\npara chegar ao imc 24"
        else:  
            classificacao = "Obesidade grau III"
            cor = "darkred"
            resultado_texto = f"Seu IMC é: {imc:.2f} \nClassificação: {classificacao} \nVocê precisa perder: {peso3:.2f} kg,\npara chegar ao imc 24"
            
        
        resultado_label.config(text=resultado_texto, fg=cor)
        messagebox.showinfo("Resultado", resultado_texto)
        
    except ValueError:
        messagebox.showwarning("Entrada inválida", "Por favor, insira valores númericos para peso e altura")
         


        
janela = tk.Tk()
janela.title("Calculadora de IMC")
janela.geometry("300x250")


tk.Label(janela, text="Peso (kg): ").pack(pady=5)
entrada_peso= tk.Entry(janela)

entrada_peso.pack(pady=5)

tk.Label(janela, text="Altura (m): ").pack(pady=5)
entrada_altura=tk.Entry(janela)
entrada_altura.pack(pady=5)

botao_calcular= tk.Button(janela, text="Calcular IMC", command=imc)
botao_calcular.pack(pady=5)

resultado_label= tk.Label(janela, text="", font=("Arial", 12))
resultado_label.pack(pady=10)

janela.mainloop()