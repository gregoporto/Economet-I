import numpy as np
import matplotlib.pyplot as plt
'''
Jeito 1 de criar gráficos -> Forma mais básica do pyplot
Extraído de https://heartbeat.fritz.ai/introduction-to-matplotlib-data-visualization-in-python-d9143287ae39
'''

x = np.linspace(0, 10, 20) # Gera 20 pontos entre 0 e 10
y = x**2 # Gera array do quadrado dos valores de x

'''
# plt.plot(x, y) # Plotando linhas
# plt.xlabel("Eixo X"), plt.ylabel("Eixo Y") # Rotulando eixos
plt.subplot (1, 2, 1) # Linhas, Colunas e Gráfico da figura
plt.plot(x, y, "red")

plt.subplot (1, 2, 2) # Linhas, Colunas e Gráfico da figura
plt.plot(x, y, "green")

plt.show()
'''

# Jeito 2 de criar gráficos -> Interface de objetos orientados (Object Oriented Interface)
fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # 4 positional args: left, bottom, width, height
ax2 = fig.add_axes([0.18, 0.55, 0.4, 0.3]) # Gráfico menor, dentro do gráfico anterior
ax.plot(x, y, "brown")
ax.set_ylabel("Eixo Y")
ax.set_xlabel("Eixo X")
ax.set_title("Curva X-Y")
ax2.plot(y, x, "blue")
plt.show()


