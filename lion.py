from collections import Counter as ct
from docx import Document as dc
from string import punctuation as pcc
import matplotlib.pyplot as plt
import pandas as pd
from openpyxl import Workbook 
from string import punctuation as pcc

document = dc('lion.docx')#Создание переменной с файлом
text_f = []#Финальная версия набора слов из документа
text_s = []#Изначальная версия
text_p = []#Промежуточная версия 

pc = pcc + '—'#Создание строки с неугодными знаками препинания 

for docxparagraph in document.paragraphs:#Файл в список
    text_s.append(docxparagraph.text)

text_s = ''.join(text_s)#Список в строку
text_s = text_s.lower()#Все слова с маленькой буквы для правильного подсчёта 

for i in text_s:
    if i not in pc:
        text_p.append(i)#Удаляем все знаки препинания 
    else:
        text_p.append(' ')#Ставим вместо них пробелы

text_p = ''.join(text_p)#Снова записываем в строку 

text_f = text_p.split()#Делим по пробелу(для избежания ошибок в определении слов)

text_len = len(text_f)#Кол-во всех слов

ish = ct(text_f)

wb = Workbook()  #Создание Excel-файла
ws = wb.active
ws.title = "Частотный список"

ws.append(["Слово", "Количество", "Процент"]) #Записываем заголовки таблицы

for nas, zn in ish.items():  #Заполняем таблицу
    prc = (zn / text_len) * 100
    ws.append([nas, zn, f"{prc:.2f}%"])

wb.save('ChastotniSpisok.xlsx')  #Сохраняем файл

letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц','ч', 'ш', 'щ', 'ь', 'ы', 'ъ', 'э', 'ю', 'я']
ish_letters = {}

str_f = ''.join(text_f)
ish_f = ct(str_f)

for i, j in ish_f.items():
    if i in letters:
        ish_letters[i] = j

sort_letters = sorted(ish_letters.keys())
plot_v = [ish_letters[letter] for letter in sort_letters]

#создание графика
plt.figure(figsize = (12, 6))
plt.bar(sort_letters, plot_v, color = 'darkcyan')
plt.xlabel('Буквы')
plt.ylabel('Количество')
plt.title('График частоты встречи букв')
plt.grid(axis = 'y')

# Отображаем график
plt.tight_layout()
plt.show()