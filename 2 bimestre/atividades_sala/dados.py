import pandas as pd 
import matplotlib.pyplot as plt

data={'Tarefa': ["Login", "Cadastro", "Logout"], "Tempo": [10,20,55]}

df= pd.DataFrame(data)

plt.bar(df["Tarefa"], df["Tempo"])
plt.title("Tempo de execução de tarefas")

plt.show()