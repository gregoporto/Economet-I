# Regressão statsmodels extraída de https://realpython.com/linear-regression-in-python/#advanced-linear-regression-with-statsmodels

# Importando os pacotes que serão usados na regressão
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Importando dados
dados = pd.read_excel(r"D:\UFS\Econometria\WAGE1.xlsx")

# Nomeando variáveis, extraindo colunas e transformando em arrays do NumPy
# Não é necessário transformar em array mas se quiser pode
sal = pd.DataFrame(dados, columns = ["salário"]) # Variável dependente
educ = pd.DataFrame(dados, columns = ["educ"]) # Variável independente
# educ, sal = np.array(educ), np.array(sal)

# Adicionando coluna com vários números 1 para statsmodels calcular o B0 (não calcula por default)
educ1 = sm.add_constant(educ)
# Pro tip: print(educ1) para entender melhor

# Fazendo o modelo
model = sm.OLS(sal, educ1)
reg = model.fit()
print(reg.summary())

# Retornando Predict e Resíduos em DataFrame
# extraído de https://stackoverflow.com/questions/32101233/appending-predicted-values-and-residuals-to-pandas-dataframe
ychap = pd.DataFrame(reg.predict())
res = pd.DataFrame(reg.resid)
# print(res)
# print(ychap)

# Plotando o gráfico de dispersão (y, x)
plt.scatter(sal, educ)

# A reta de regressão tem que ser calculada com os valores previstos (ychap, x)
#plt.plot(ychap, educ)
#plt.show()

# Também pode ser calculada com atributo .fittedvalues do statsmodels
plt.plot(reg.fittedvalues, educ)
plt.show()



