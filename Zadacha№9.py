# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

print('Введите номер четверти от 1 до 4')
Part = int(input())
match Part:
    case 1:
        print('Диапазон точек от: x(1,Бесконечности), и y(1,Бесконечности)')
    case 2:
        print('Диапазон точек от: x(1,-Бесконечности), и y(1,Бесконечности)')
    case 3:
        print('Диапазон точек от: x(1,-Бесконечности), и y(1,-Бесконечности)')
    case 4:
        print('Диапазон точек от: x(1,Бесконечности), и y(1,-Бесконечности)')
    case _:
        print('Координатная плоскость имеет всего 4 части(четверти). Введите значение от 1 до 4!')

