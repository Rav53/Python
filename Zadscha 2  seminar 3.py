# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
list = list(map(int, input("Введите числа через пробел:\n").split()))
final_list = []
for i in range((len(list)+1)//2):
    final_list.append(list[i]*list[len(list)-1-i])
print(final_list)