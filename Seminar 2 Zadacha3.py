# Задайте список (словарь не нужно выводить!)
# из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

n = int(input('Введите число: ')) 

def sequence(n):
    return[round((1 + 1 / n)**n, 2)for n in range (1, n + 1)]   
        
print(sequence(n))
print(round(sum(sequence(n))))