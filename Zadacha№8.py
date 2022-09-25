# №8 Напишите программу, которая принимает на вход
# координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт
# номер четверти плоскости, в которой находится эта точка
# (или на какой оси она находится).

print('Введите координаты х и у')
coordinate = [int(input()), int(input())]
if coordinate[0] > 0 and coordinate[1] > 0:
    print('Четверть № -', 1)
elif coordinate[0] < 0 and coordinate[1] < 0:
    print('Четверть № -', 3)
elif coordinate[0] > 0 and coordinate[1] < 0:
    print('Четверть № -', 4)
else:
    print('Четверть № -', 2)