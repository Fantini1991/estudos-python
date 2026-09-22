import pandas as pd

tabela = pd.read_csv("medicoes.csv")

tabela["temperatura_k"] = tabela["temperatura"] + 273.15
tabela["status"] = "OK"

tabela.loc[ (tabela ["ph"] < 6.5) | (tabela ["ph"] > 7.5), "status" ] = "FORA"
resumo_lote = tabela.groupby("lote")["ph"].agg(["count", "mean", "median", "min", "max"])
lotes_fora = tabela.groupby("lote")["status"].value_counts()

print(tabela)
print()
print(resumo_lote)
print()
print(lotes_fora)