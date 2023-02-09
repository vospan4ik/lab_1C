"""
Написать программу без использования библиотек, классов и функций в которую пользователь вводит две строки неограниченной длины, содержащие версии программ.
Версия программы – это строка их 4-х чисел, разделенных точками. Числа целые положительные или ноль. Могут начинаться с нулей. Обработка должна определить, какая из версий старше. Показать несколько примеров.
Примеры версий (этот пример в видео тоже показать):
8.1.13.41
8.1.009.125
Важное уточнение: лидирующие нули не играют роли в определении версии, то есть версии "001.2.3" и "1.2.3" одинаковые.
"""

# ввод версий программ, их перевод в списки
v_1 = [int(num) for num in input('Введите первую версию: ').split('.')]
v_2 = [int(num) for num in input('Введите вторую версию: ').split('.')]

# сравнение списков по старшинству
if v_1 > v_2:
    print('Более старшая версия:')
    print(*v_1, sep='.')
elif v_2 > v_1:
    print('Более старшая версия:')
    print(*v_2, sep='.')
else:
    print('Версии одинаковые:')
    print(*v_1, sep='.')