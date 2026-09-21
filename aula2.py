# Calculo de concentracao molar e diluicao
massa_soluto = float(input("Massa do soluto (g): "). replace(",", "."))      # gramas de NaCl
massa_molar = float(input("Massa molar (g/mol): "). replace(",", "."))       # g/mol
volume_1 = float(input("Volume 1 (L): "). replace(",", "."))                 # litros (V1)
volume_2 = float(input("Volume 2 (L): "). replace(",", "."))                 # litros (V2, volume final)

mols = massa_soluto / massa_molar
concentracao_1 = mols / volume_1                        # C1
concentracao_2 = concentracao_1 * volume_1 / volume_2   # C2 = C1 * V1 / V2

print("Mols de soluto:", mols)
print("Concentracao C1 (mol/L):", concentracao_1)
print("Concentracao C2 (mol/L):", concentracao_2)