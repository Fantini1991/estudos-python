import sqlite3
import pandas as pd

tabela = pd.read_csv("medicoes.csv")

conexao = sqlite3.connect("lab.db")
tabela.to_sql("medicoes", conexao, if_exists="replace", index=False)

resultado_1 = pd.read_sql("SELECT amostra, ph FROM medicoes WHERE ph < 6.5 OR ph > 7.5 ", conexao)

resultado_2 = pd.read_sql("""
SELECT lote, COUNT(*), AVG(ph) AS media_ph
FROM medicoes
GROUP BY lote
ORDER BY media_ph DESC
""", conexao)

print(resultado_1)
print()
print(resultado_2)

conexao.close()