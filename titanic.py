import matplotlib.pyplot as plt
import pandas as pd

# Преобразование parquet в csv
parquet = pd.read_parquet('titanic.parquet')
parquet.to_csv('titanic.csv', index = False)

parquet = pd.read_csv('titanic.csv') # Чтение данных

survivours = parquet.groupby(['Pclass', 'Survived']).size().unstack(fill_value = 0)#новая таблица

survivours_percent = survivours.div(survivours.sum(axis = 1), axis = 0) * 100 # проценты в оси y

#график
survivours_percent.plot(kind = 'bar', stacked = True, color = ['orangered', 'forestgreen'])
plt.title('Процент выживших пассажиров Титаника по классам билетов')
plt.xlabel('Класс билета')
plt.ylabel('Процент пассажиров')
plt.xticks(rotation = 0)  # Поворот меток оси X
plt.legend(['Не выжил', 'Выжил'])  # Легенда

plt.show()