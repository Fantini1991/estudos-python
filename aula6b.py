import pandas as pd

tabela = pd.read_csv("medicoes.csv")

tabela["temperatura_k"] = tabela["temperatura"] + 273.15
tabela["status"] = "OK"

tabela.loc[ (tabela ["ph"] < 6.5) | (tabela ["ph"] > 7.5), "status" ] = "FORA"
resumo_lote = tabela.groupby("lote")["ph"].agg(["count", "mean", "median", "min", "max"])
lotes_fora = tabela.groupby("lote")["status"].value_counts()

status_fora = tabela[tabela["status"] == "FORA"]
status_fora_por_lote = status_fora.groupby("lote")["status"].count()

print(tabela)
print()
print(resumo_lote)
print()
print(lotes_fora)
print()
print(status_fora_por_lote)

import matplotlib.pyplot as plt

plt.bar(status_fora_por_lote.index, status_fora_por_lote.values)
plt.title("Amostras fora da faixa de pH, por lote")
plt.ylabel("Quantidade fora da faixa")
plt.xlabel("Lote")
plt.savefig("grafico_fora_por_lote.png")
plt.show()