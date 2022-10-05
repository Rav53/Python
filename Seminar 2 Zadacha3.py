# Задайте список (словарь не нужно выводить!)
# из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
n = int(input('Введите число: ')) 

def list(n):
    return[round((1 + 1 / n)**n, 2)for n in range (1, n + 1)]   
print(list(n))
print(round(sum(list(n))))

# def newNum(n):
#     if n == 1:
#         return 1
#     else:
#         return round((1+1/n)**n, 2)


# num = int(input("Введите число: "))

# list = []
# for i in range(1, num + 1):
#     list.append(newNum(i))
# print(list)
# print(f"Сумма элементов последовательности равна: {sum(list)}")
