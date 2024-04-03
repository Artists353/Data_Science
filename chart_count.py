import matplotlib.pyplot as plt

num_avto = [24, 56, 78, 21]
avto = ['BMW', 'AUDI', 'Jaguar', 'Mersedes']

plt.pie(num_avto, labels=avto, autopct='%1.1f%%')
plt.title('Кол-во авто на дороге')
plt.show()