import os
from threading import Thread
from main import pdf_ex

# Путь к папке с чертежами
put_in = 'чертежи\\Чертежи для А'
# Список файлов PDF
fil = []
# Список путей к excel1
ex = []
# Список путей к выходным excel файлам
ex_out = []
# Перебор всех файлов в папке
for root, dirs, fiels in os.walk(put_in):
    for i in fiels:
        # Проверка, является ли файл PDF
        if '.pdf' in i:
            # Добавление пути к файлу PDF в список
            fil.append(root + '\\' + i)
            # Формирование пути к папке excel1
            put = root + '\\' + i
            put1 = root.split('\\')
            put1[1] = 'excel1'
            # Добавление пути к excel1 в список
            pyt_ex = '\\'.join(put1)
            ex.append(pyt_ex)
            # Добавление пути к выходному excel файлу в список
            ex_out.append(pyt_ex + '\\' + i[:-4])
# Уникальные пути к excel1
exz = list(set(ex))
# Создание папок excel1
for j in exz:
    os.makedirs(j, exist_ok=True)

print(len(fil))
# Функция для выполнения обработки PDF файлов
def many_y(put_in,put_out):
    u = 0
    for in_a, out_a in zip(put_in,put_out):
        u+=1
        print(in_a)
        print(f'{u} из {len(put_in)}')
        # Вызов функции обработки PDF файла
        pdf_ex(in_a,out_a)
#

# Запуск обработки файлов
many_y(fil,ex_out)

# для запуска в 4 потока
# l = int(len(fil)/4)
# print(l)
# in1 = fil[0:l]
# ex_out1 = ex_out[0:l]
#
# in2 = fil[l:l*2]
# ex_out2 = ex_out[l:l*2]
#
# in3 = fil[l*2:l*3]
# ex_out3 = ex_out[l*2:l*3]
#
# in4 = fil[l*3:len(fil)]
# ex_out4 = ex_out[l*3:len(fil)]
#
#
#
# thread1 = Thread(target=many_y, args=(in1,ex_out1))
# thread2 = Thread(target=many_y, args=(in2,ex_out2))
# thread3 = Thread(target=many_y, args=(in3,ex_out3))
# thread4 = Thread(target=many_y, args=(in4,ex_out4))
#
# thread1.start()
# thread2.start()
# thread3.start()
# thread4.start()
# thread1.join()
# thread2.join()
# thread3.join()
# thread4.join()
