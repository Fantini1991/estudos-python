from scipy import stats

pesos = [498, 505, 495, 510, 502]

resultado = stats.ttest_1samp(pesos, popmean=500)
print(resultado)

from scipy import stats

ph_l2 = [7.3, 10.01, 7.0]

resultado = stats.ttest_1samp(ph_l2, popmean=7.5)
print(resultado)