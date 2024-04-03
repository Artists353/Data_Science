import matplotlib.pyplot as plt

y = ['Январь', 'Февраль', 'Март']
x = [3000, 5000, 3000]


plt.bar(y, x, label='Доходы в рублях', alpha=0.5)
plt.plot(y, x, color='green', marker='o', markersize=7)
plt.title('Диаграмма заработка')
plt.ylabel('Чистый доход')
plt.xlabel('2024 год')
plt.legend()
plt.show()