"""
Реализовать функцию перевода числа в строковое представление, без использования встроенных функции языка программирования, если такие есть в явном виде (Например, для 1С без использования функции ЧислоПрописью). Показать несколько примеров.
Пример: 1020 - > «Одна тысяча двадцать».
Число целое положительное или ноль.
Не больше 100 000 000, но программа должна ЛЕГКО расширяться для добавления больших чисел. Это очень важное условие.
"""
# словарь цифр
d_digit = {
    0: '',
    1: 'один',
    2: 'два',
    3: 'три',
    4: 'четыре',
    5: 'пять',
    6: 'шесть',
    7: 'семь',
    8: 'восемь',
    9: 'девять',
    10: 'десять',
    11: 'одиннадцать',
    12: 'двенадцать',
    13: 'тринадцать',
    14: 'четырнадцать',
    15: 'пятнадцать',
    16: 'шестнадцать',
    17: 'семнадцать',
    18: 'восемнадцать',
    19: 'девятнадцать',
    20: 'двадцать',
    30: 'тридцать',
    40: 'сорок',
    50: 'пятьдесят',
    60: 'шестьдесят',
    70: 'семьдесят',
    80: 'восемьдесят',
    90: 'девяносто',
    100: 'сто',
    200: 'двести',
    300: 'триста',
    400: 'четыреста',
    500: 'пятьсот',
    600: 'шестьсот',
    700: 'семьсот',
    800: 'восемьсот',
    900: 'девятьсот',
}

# словарь рангов: тысячи и миллионы, также сюда добавлять разряды для бОльших чисел
d_rank = {
    1: ['одна тысяча', 'две тысячи', 'три тысячи', 'четыре тысячи', 'тысяч'],
    2: ['один миллион', 'два миллиона', 'три миллиона', 'четыре миллиона', 'миллионов'],
}


# определение трехзначного числа
def define_num(number):
    if number == 0:
        return 'ноль'
    if number <= 20:
        return d_digit[number]
    elif 20 < number <= 99:
        return d_digit[(number // 10) * 10] + ' ' + d_digit[number % 10]
    elif number % 100 == 0:
        return d_digit[number]
    elif 100 < number <= 999 and 10 <= number % 100 <= 19:
        return (d_digit[(number // 100) * 100] + ' ' + d_digit[(number % 100)]).strip()
    elif 100 < number <= 999 and number % 100 > 19 or number % 100 < 10:
        return (d_digit[(number // 100) * 100] + ' ' + d_digit[((number // 10) % 10) * 10] + ' ' + d_digit[number % 10]).replace('  ', ' ')


# корректировка окончаний для конкретрных случаев с 1 - 4
def correct_word(word):
    if 'один тысяч' in word:
        word = word.replace('один тысяч', d_rank[1][0])
    elif 'два тысяч' in result:
        word = word.replace('два тысяч', d_rank[1][1])
    elif 'три тысяч' in result:
        word = word.replace('три тысяч', d_rank[1][2])
    elif 'четыре тысяч' in result:
        word = word.replace('четыре тысяч', d_rank[1][3])

    if 'один миллионов' in result:
        word = word.replace('один миллионов', d_rank[2][0])
    elif 'два миллионов' in result:
        word = word.replace('два миллионов', d_rank[2][1])
    elif 'три миллионов' in result:
        word = word.replace('три миллионов', d_rank[2][2])
    elif 'четыре миллионов' in result:
        word = word.replace('четыре миллионов', d_rank[2][3])
    return word


num = int(input('Введите число: '))

if num < 1000:
    print(define_num(num))
else:
    num_list = []
    while num > 0:
        num_list.append(num % 1000)
        num = num // 1000

    answer = []
    for i in range(len(num_list)):
        if num_list[i] == 0:
            continue
        elif num_list[i] > 0 and i > 0:
            answer.append(d_rank[i][4])
            answer.append(define_num(num_list[i]))
        elif num_list[i] > 0:
            answer.append(define_num(num_list[i]))

    result = ' '.join(answer[::-1])

    print(correct_word(result))
