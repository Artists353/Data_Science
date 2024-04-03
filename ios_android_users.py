import matplotlib.pyplot as plt

years = ['2017', '2018', '2019', '2020', '2021']
android_users = [87, 56, 78, 90, 180]
ios_users = [45, 120, 30, 87, 67]

width = 0.35
fig, ax = plt.subplots()

ax.bar(years, android_users, width, label='Андройд')
ax.bar(years, ios_users, width, bottom=android_users, label='Ios')
ax.set_ylabel('Соотношение в %')
ax.set_title('Распределено в каких годах лучше продавались смартфоны')
ax.legend(loc='lower left', title='Устройства')

plt.show()