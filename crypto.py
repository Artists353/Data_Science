import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 10, 25, 32, 30, 24, 10]

plt.plot(x, y, color='green', marker='o', markersize=7)
plt.ylabel('Y')
plt.xlabel('X')
plt.title('Pov cripto')
plt.show()