import sqlite3
import pandas as pd

medicoes = pd.read_csv("medicoes.csv")
lotes = pd.read_csv("lotes.csv")

conexao = sqlite3.connect("lab.db")
medicoes.to_sql("medicoes", conexao, if_exists="replace", index=False)
lotes.to_sql("lotes", conexao, if_exists="replace", index=False)
resultado = pd.read_sql("""
    SELECT medicoes.amostra, medicoes.ph, lotes.responsavel
    FROM medicoes
    JOIN lotes ON medicoes.lote = lotes.lote
""", conexao)

print(resultado)

resultado_1 = pd.read_sql("""
    SELECT medicoes.amostra, medicoes.ph, lotes.responsavel
    FROM medicoes
    JOIN lotes ON medicoes.lote = lotes.lote
    WHERE medicoes.ph < 6.5 OR medicoes.ph > 7.5
""", conexao)
print(resultado_1)

conexao.close()