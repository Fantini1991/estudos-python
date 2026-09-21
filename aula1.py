#Calculo de Concentração molar
massa_soluto = 5.85     # gramas de NaCL
massa_molar = 58.44     # g/mol
volume_1 = 0.5          # litros (V1)
Volume_2 = 2            #litros (v2)

mols = massa_soluto / massa_molar
Concentracao_1 = mols / volume_1                                #c1
Concentracao_2 = Concentracao_1 * volume_1 / Volume_2         #c2= c1 * v1 / v2


print("Mols de soluto:", mols)
print("Concentracao c1(mol/L):", Concentracao_1)
print("Concentracao C2 (mol/L)", Concentracao_2)

