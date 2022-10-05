# Напишите программу, которая будет 
# преобразовывать десятичное число в двоичное.

number_a = int(input('Введите число в десятичной системе счисления: '))
number_b = ''
while number_a > 0:
    number_b = str(number_a % 2) + number_b
    number_a = number_a // 2
print('Число в двоичной системе:',number_b)


# Классное решение нашёл)):
# n = int(input('Введите число: '))
# print(bin(n))


