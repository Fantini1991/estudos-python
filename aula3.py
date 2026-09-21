# Medicoes de pH de 7 amostras
ph_amostras = [6.8, 7.1, 6.9, 7.3, 7.0, 5.4, 10.01]

soma = 0

for ph in ph_amostras: 
    print("pH da amostra:", ph)
    soma = soma + ph
    if ph < 6.5 or ph > 7.5:
       print("  ATENCAO: fora da faixa!")

media = soma / len(ph_amostras)
print("pH medio:", media)
print("Maior pH:", max(ph_amostras))
print("Menor pH:", min(ph_amostras))