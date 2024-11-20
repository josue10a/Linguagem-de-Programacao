import tkinter as tk
from tkinter import ttk, messagebox

# Função para mudar para a próxima janela
def open_calculator():
    main_window.withdraw()  # Fecha a janela inicial
    calculator_window.deiconify()  # Mostra a janela da calculadora

# Função para calcular o IMC
def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        nome=str(entry_nome.get())
        if peso <= 0 or altura <= 0:
            raise ValueError
        imc = peso / (altura ** 2)
        if imc < 18.5:
            categoria = "Abaixo do peso 🥗"
        elif 18.5 <= imc < 24.9:
            categoria = "Peso normal 🌟"
        elif 25 <= imc < 29.9:
            categoria = "Sobrepeso 🍔"
        else:
            categoria = "Obesidade ⚠"
        
        resultado_label.config(
            text=f"Seu Nome: {nome} \n Seu IMC: {imc:.2f}\nCategoria: {categoria}", 
            foreground="blue"
        )
    except ValueError:
        messagebox.showerror("Erro de entrada", "Insira valores válidos para peso e altura.")
        
#função fechar janela

def fechar():
    main_window.withdraw()
    
#função fechar janela 1

def fechar1():
    calculator_window.withdraw()

# Função para voltar à tela inicial
def voltar_inicio():
    calculator_window.withdraw()  # Fecha a janela da calculadora
    main_window.deiconify()  # Mostra a janela inicial

# Criação da janela principal
main_window = tk.Tk()
#mudei a cor de fundo para preta da janela principal e altura e tamanho
main_window.configure(bg="black")
main_window.title("Calculadora de IMC")
main_window.geometry("500x400")
main_window.resizable(False, False)

# Design da janela principal, adicionei cor de fundo  e cor de fonte 
titulo_label = tk.Label(main_window, text="Bem-vindo(a)!", font=("Arial", 25, "bold"), bg="black", fg="white")
titulo_label.pack(pady=20)

#adicionei cor de fundo  e cor de fonte e o pady 
descricao_label = tk.Label(main_window, text="Descubra seu IMC e a categoria correspondente.", font=("Arial", 13, "normal" ), bg="black", fg="white")
descricao_label.pack(pady=20)

#mudei o pady, o tamanho e altura do botão e o tamanho da fonte, além da cor do botão e a cor da fonte, além de adicionar uma cor diferente a fonte quando o usuário clica nele e troquei de ttk.button para tk.button, pois o ttk não suporta bg nem fg pois é nativo do sistema operacional
comecar_button = tk.Button(main_window, text="Começar Agora", font=("Arial", 17, "normal"), bg="#50C878", fg="white", activeforeground="red", width="25", height="1", command=open_calculator)
comecar_button.pack(pady=30)

#botão para fechar janela, mudei o pady, o tamanho e altura do botão e o tamanho da fonte, além da cor do botão e a cor da fonte, além de adicionar uma cor diferente a fonte quando o usuário clica nele e troquei de ttk.button para tk.button, pois o ttk não suporta bg nem fg pois é nativo do sistema operacional
fechar_janela=tk.Button(main_window, text="Fechar janela",font =("Arial", 17, "normal"),bg="#50C878", fg="white", activeforeground="red" , width="25", height="1", command=fechar)
fechar_janela.pack(pady=30)


# Criação da segunda janela (calculadora), mesmas alterações da primeira
calculator_window = tk.Toplevel(main_window)
calculator_window.title("Calculadora de IMC")
calculator_window.geometry("500x500")
calculator_window.resizable(False, False)
calculator_window.withdraw()  # Oculta esta janela no início
calculator_window.configure(bg="black")#mudar cor de fundo


# Design da calculadora
titulo_calculadora = tk.Label(calculator_window, text="Calculadora de IMC", font=("Arial", 25, "bold"), bg="black", fg="white")
titulo_calculadora.pack(pady=20)

# Entrada para nome

nome_frame=tk.Frame(calculator_window)
nome_frame.pack(pady=3)
label_nome=tk.Label(nome_frame, text="Nome:      ", font=("Arial", 15), fg="white", bg="black")
label_nome.pack(side="left")
entry_nome=ttk.Entry(nome_frame, font=("Arial", 15))
entry_nome.pack(side="left")

# Entrada para peso
peso_frame = tk.Frame(calculator_window)
peso_frame.pack(pady=3)
label_peso = tk.Label(peso_frame, text="Peso (kg):", font=("Arial", 15), fg="white", bg="black")
label_peso.pack(side="left")
entry_peso = ttk.Entry(peso_frame, font=("Arial", 15))
entry_peso.pack(side="left")

# Entrada para altura
altura_frame = tk.Frame(calculator_window)
altura_frame.pack(pady=3)
label_altura = tk.Label(altura_frame, text="Altura (m):", font=("Arial", 15), bg="black", fg="white")
label_altura.pack(side="left")
entry_altura = ttk.Entry(altura_frame, font=("Arial", 15))
entry_altura.pack(side="left")




# Botão de calcular
calcular_button = tk.Button(calculator_window, text="Calcular IMC", font =("Arial", 17, "normal"),bg="#50C878", fg="white", activeforeground="red" , width="25", height="1", command=calcular_imc)
calcular_button.pack(pady=10)

# Exibição do resultado
resultado_label = tk.Label(calculator_window, text="", font=("Arial", 14, "bold"), bg="black")
resultado_label.pack(pady=10)

# Botão para voltar
voltar_button = tk.Button(calculator_window, text="Voltar",  font =("Arial", 17, "normal"),bg="#50C878", fg="white", activeforeground="red" , width="25", height="1",command=voltar_inicio)
voltar_button.pack(pady=10)

#adicionei o botão fechar janela, igual da primeira 

fechar_janela1=tk.Button(calculator_window, text="Fechar janela",font =("Arial", 17, "normal"),bg="#50C878", fg="white", activeforeground="red" , width="25", height="1", command=fechar1)
fechar_janela1.pack(pady=5)

# Rodapé
footer_label = tk.Label(calculator_window, text="Desenvolvido por Josué, juntamente com Romes.Todos os direitos reservados © 2024, 😊", font=("Arial", 8), fg="white", bg="black")
footer_label.pack(side="bottom", pady=10)

# Loop principal
main_window.mainloop()