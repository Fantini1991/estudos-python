import pandas as pd
import matplotlib.pyplot as plt

tabela = pd.read_csv("medicoes.csv")

print(tabela)
print()
print("Media do pH por lote:")
print(tabela.groupby("lote")["ph"].mean())

plt.bar(tabela["amostra"], tabela["ph"])
plt.axhline(6.5, color="red", linestyle="--")
plt.axhline(7.5, color="red", linestyle="--")
plt.title("pH por amostra")
plt.ylabel("pH")
plt.savefig("grafico_ph.png")
plt.show()