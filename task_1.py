"""
Дано целое число k > 2. Напечатать все числа из диапазона 2, k, не являющиеся простыми. Показать несколько примеров.
"""

# проверям, простое ли число
def is_prime(x):
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return False
    return True


k = int(input('Введите число k = '))

for i in range(2, k + 1):
    if not is_prime(i):
        print(i, end=' ')