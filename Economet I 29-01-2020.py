import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
#
dados = pd.read_excel(r"D:\UFS\Econometria\Salário e Educação.xlsx")
y = pd.DataFrame(dados, columns = ["Salario"]) # Variável dependente
x = pd.DataFrame(dados, columns = ["Estudo"]) # Variável independente
X = sm.add_constant(x)
#
reg = sm.OLS(y, X)
rst = reg.fit()
#print(rst.summary())
'''
fig, ax = plt.subplots(figsize = (8,6)) # Plotando 800x600
ax.scatter(x, y, label = "dados", c = "slateblue") # Plotando dispersão
#ax.plot(x, rst.fittedvalues, 'g--', label = "Reg") # Plotando reta de regressão com fitted values
ax.plot(x, rst.predict(), 'gray--', label = "Reg") # Plotando reta de regressão com fitted values
ax.legend(loc = "best") # Colocando legenda top left
plt.show()
'''

# Predict, Resíduos e Soma dos Quadrados dos Resíduos (SQRes)
res = pd.DataFrame(rst.resid)
sqres = np.sum(res**2)
print(f"Os resíduos são: {res}")
print(f"A soma dos quadrados dos resíduos é: {sqres}.")

# Variância Chapeu / Sigma Chapeu
var = sqres / (reg.nobs - 2)
print(f"Sigma chapeu é: {var}.")

# Erro Padrão -> Raiz quadrada da variância
ep = np.sqrt(var)
print(f"O erro padrão é: {ep}.")

# Média dos valores de X
xmean = np.mean(x)
print(f"A média dos valores de X é: {xmean}.")

# Soma do Quadrado do Desvio de X
sqdvx = np.sum( (np.std(x))**2 )*10 # O 'x10' foi adicionado depois, não sei pq o resultado deu 10x menor!
print(f"A soma dos quadrados do Desvio de X é: {sqdvx}.")

# Variância de Beta 1 chapéu / Var(B1)^
varB1c = var / sqdvx
print(f"A variância do estimador de Beta 1 é: {varB1c}.")

# Erro Padrão de Beta 1 chapéu / EP(B1)^
epb1c = np.sqrt(varB1c)
print(f"O erro padrão de Beta 1 chpaéu é: {epb1c}.")

