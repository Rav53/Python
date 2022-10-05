# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.



from ast import While
from tokenize import Number
from typing import List


def Fibon_NegaF(Number):
    if Number == 0:
        return 0
    Negafibonach = False
    if Number < 0:
        Negafibonach = True
        Number *= -1

    f1 = 1
    f2 = 1
    i = 0
    while i < Number - 2:
        f_sum = f1 + f2
        f1 = f2
        f2 = f_sum
        i = i+1
    if Negafibonach:
        f2 = (-1)**(Number+1) * f2
    return f2
    
List_Fibo = []

Imput_error = True
while Imput_error:
    Len_list = input('Введите длинну списка: ')
    try:
        Len_list = int(Len_list)
        if Len_list <= 0:
            print('Нужно ввести число больше нуля: ')
            Imput_error = True
        else:
            Imput_error = False
    except ValueError:
        print('Ошибочный ввод, повторите попытку: ')
for i in range(-Len_list, Len_list+1):
    List_Fibo.append(Fibon_NegaF(i))
print(f'Список чисел Фибоначчи от: -{Len_list} до {Len_list}')
print(List_Fibo)