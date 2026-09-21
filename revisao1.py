# Temperatura do Forno

temperaturas = [850, 872, 910, 895, 930, 865]
soma = sum(temperaturas)
quantidade = len(temperaturas)
temperatura_media = (soma / quantidade)

contador = 0

for temperatura in temperaturas:
    if temperatura > 900:
        contador = contador + 1

print("Temperatura média:", temperatura_media)
print("Leituras acima de 900:", contador)
print("Temperatura Máxima:", max(temperaturas))