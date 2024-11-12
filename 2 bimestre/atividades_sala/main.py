import tkinter as tk
from tkinter import messagebox

#Função que será executada quando o botão for pressionado
def mostrar_mensagem():
    nome = entrada_nome.get()
    if nome == "":
        messagebox.showwarning("Atenção", "Digite um nome!")
    else:
        mensagem = f"Olá, {nome}!"
        messagebox.showinfo("Mensagem", mensagem)

# Configuração da janela principal
janela = tk.Tk()
janela.title("Olá, Python!")
janela.geometry("300x200")

# Criação de um rótulo para instrução
rotulo = tk.Label(janela, text="Digite seu nome:")
rotulo.pack(padx=10, pady=10)

# Criação de uma entrada de texto
entrada_nome = tk.Entry(janela)
entrada_nome.pack(padx=10, pady=10)

# Criação de um botão para exibir a mensagem
botao = tk.Button(janela, text="Exibir mensagem", command=mostrar_mensagem)
botao.pack(padx=10, pady=10)

# Iniciar a aplicação
janela.mainloop()