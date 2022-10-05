# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.

list = list(map(float, input("Введите вещественные числа через пробел:\n").split()))
final_list = []
min = 1
max = 0
for i in list:
    if (i - int(i)) <= min:
        min = i - int(i)
    if (i - int(i)) >= max:
        max = i - int(i) 
print('Разница:',(round((max-min),2)))
