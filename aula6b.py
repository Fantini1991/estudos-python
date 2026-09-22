import pandas as pd

tabela = pd.read_csv("medicoes.csv")

tabela["temperatura_k"] = tabela["temperatura"] + 273.15

print(tabela)