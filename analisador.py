def classificar_ph(ph):
    if ph < 6.5 or ph > 7.5:
        return "FORA"
    else:
        return "OK"

print(classificar_ph(7.0))
print(classificar_ph(9.5))
print(classificar_ph(6.0))

import pandas as pd
import matplotlib.pyplot as plt

tabela = pd.read_csv("medicoes.csv")
tabela["status"] = tabela["ph"].apply(classificar_ph)

print(tabela)

while True:
    print("1. ver tabela")
    print("2. Ver resumo por lote")
    print("3. Gerar grafico")
    print("4. Consultar com SQL")
    print("0. Sair")
    escolha = input("Escolha: ")

    if escolha == "1":
        print(tabela)
    elif escolha == "2": 
        resumo_lote = tabela.groupby("lote")["ph"].agg(["count", "mean", "median", "min", "max"])
        print(resumo_lote)
    elif escolha == "3":
        fora_por_lote = tabela[tabela["status"] == "FORA"].groupby("lote")["status"].count()
        plt.bar(fora_por_lote.index, fora_por_lote.values)
        plt.title("Amostras fora da faixa de pH, por lote")
        plt.savefig("grafico_fora_por_lote.png")
        plt.show()
        print("Grafico salvo em grafico_fora_por_lote.png")
    elif escolha == "4":
        import sqlite3
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
        print(resultado_2)
    elif escolha == "0":
        break
    else:
        print("Opção invalida")