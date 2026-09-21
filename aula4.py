import pandas as pd

dados = {
    "amostra": ["A1", "A2", "A3", "A4", "A5"],
    "ph": [6.8, 7.1, 5.4, 7.3, 10.01],
    "temperatura": [25.0, 25.5, 24.8, 26.1, 25.2],
    "condutividade": [5, 7, 9, 10, 4],
}

tabela = pd.DataFrame(dados)

print(tabela)
print()
print("Media do pH:", tabela["ph"].mean())
print()
print("Amostras fora da faixa:")
print(tabela[(tabela["ph"] < 6.5) | (tabela["ph"] > 7.5)])
print("Condutividade maxima:", tabela["condutividade"].max())
print(tabela[(tabela["temperatura"] >= 25)])