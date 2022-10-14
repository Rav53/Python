# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
import itertools as it


def ratios_list(k):
    ratios = [randint(0, 10) for i in range(k + 1)]
    if ratios[0] == 0:
        ratios[0] = randint(1, 10)
    return ratios


def polynom_list(cof, ratios):
    op = ['*x^']*(cof-1) + ['*x']
    polynom = [[a, b, c] for a, b, c in it.zip_longest(
        ratios, op, range(cof, 1, -1), fillvalue='') if a != 0]
    for x in polynom:
        x.append(' + ')
    polynom = list(it.chain(*polynom))
    polynom[-1] = ' = 0'
    return "".join(map(str, polynom)).replace(' 1*x', ' x')


cof = randint(2, 5)
ratios = ratios_list(cof)
polynom = polynom_list(cof, ratios)
print(polynom)

with open('Polynom_33.txt', 'w') as data:
    data.write(polynom)