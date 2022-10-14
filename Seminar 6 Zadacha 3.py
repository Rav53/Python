# Даны два файла в каждом из которых находится запись многочлена.
#  Сформировать файл содержащий сумму многочленов.

def Get_Stepen(string,Pol_X):                                 #функция определяет значение степени для конкретного положения Х
    if string[Pol_X + 1] ==' ':                               # Если справа от х пусто то степень 1
        return 1
    elif string[Pol_X + 1] == '^':                            # Если справа от х ^ то продолжаем анализ
        End_Step = True
        count = 0
        while End_Step:                                       # ведем подсчет символов до нахождения первого ' '
            count += 1
            if string[Pol_X + 1 + count] ==' ':
                End_Step = False                              # Заканчиваем посчет
    else: return 0                                            # Выводим 0 при неверных данных ввода
    return int(string[Pol_X + 2 : Pol_X + count + 1])         # Выдаем число равное степени х


def Get_Coefficient(string,Pol_X):              # функция определяет значение коэфициента для конкретного положения Х
    if Pol_X == 0 or string[Pol_X-1] == ' ':    # проверяем положение х, если х в начале строки('х + 1 = 0') то коэфициент = 1 или если перед х ' '('10 + x = 0') то коэфициент = 1
        return 1
    elif string[Pol_X-1] == '*':                # Проверяем наличие перед х знака множителя(основное условие для того что множитель > 1)
        End_Step = True                                         
        count = 1
        while End_Step:                         # проводим  подсчет символов до нахождения первого ' ' или начала строки 
            count += 1
            if Pol_X - count < 0 or Pol_X - count == ' ':
                End_Step = False    
    else: 
        return -1                                # Выводим -1 при неверных данных ввода
    return int(string[Pol_X - count+1:Pol_X-1]) # Выдаем число равное коэфициенту перед х

def Get_Coefficient_X0(string):             # Функция определения коэфициента при х^0 на входе может быть  '= 0' или ' + 1 = 0' или '1 = 0'
    if string[0] == '=':                    # Если на входе '= 0' то коэфициент при х^0 равен 0
        return 0
    else:                                   # Если на входе ' + 1 = 0' или '1 = 0' то коэфициент при х^0 высчитывается начиная с символа  =   строки до следующего пробела (т.е. 1)
        End_Step = True
        count = string.find('=') - 2
        while End_Step:
            count -= 1                     
            if count == -1:                  # если на входе  '1 = 0'
                End_Step = False
            elif string[count] ==' ':       # ведем подсчет символов до нахождения первого ' '  Если на входе ' + 1 = 0'
               End_Step = False 
    return int(string[count + 1: string.find('=') - 1:])            # выводим коэфициент при х^0 длина числа неважна    (только если она не больше типа int)

def Obrezka_strok(string, Start, Length):   # Функция обрезки строки по операнду х и его степени
    Step = ''
    if Length == 1:                         # если степень х равна 1 то строка 'x + 1 = 0'  после обрезки будет выглятеть  '1 = 0'
        Step = '  '
    elif len(string[Start + Length + 1:]) <5:    # 6*x^3 = 0 после обрезки будет выглятеть  '= 0'
        Step = str(Length) + '   '
    else:
        Step = str(Length) + '   + '                         
    return  string[Start + len(Step):]                          # str1 = '6*x^3 + 4*x^2 + x + 1 = 0' после обрезки будет выглятеть  ' + 1 = 0'    


with open('Многочлен 1.txt') as f:
    str1 = f.readline()
with open('Многочлен 2.txt') as f:
    str2 = f.readline()
print('Из файла Многочлен 1.txt получена следующая строка с уравнением: ', end='')
print(str1)
print('Из файла Многочлен 2.txt получена следующая строка с уравнением: ', end='')
print(str2)
 #Основной код программы суммирования уровнений

if str1.find('x') == -1 or str2.find('x') == -1 or len(str1) < 5 or len(str2) < 5:          # Проверка вводных данных в строке должен быть хоть 1 х, длина строки не менее 5 символов
    print('Ошибка вводных данных! Один или оба файла не содержат уравнение типа х2 + х + 1 = 0 ')
    exit()
Cicle1_end = False              # операнд выхода из цикла  
Cicle2_end = False              # операнд выхода из цикла
Cicle_end = True                # операнд выхода из цикла
New_STRING = ''                    # строка для суммирования уравнений
Plus = ''                       # переменная для введения знака + в новую строку
while   Cicle_end:                  # Цикл прохода по х в строках str1 и str2 с последующим суммированием и сохранением результата в строку New_STRING
    X1 = str1.find('x')
    X2 = str2.find('x')
    if X1 == -1:                    # при переборе в str1 х не обнаружено срабатывает первый операнд выхода из цикла
        Cicle1_end = True
        Stepen_in_Str1 = 0            #  при отсутствии х степень   становится = 0
        Coefficient_in_Str1 = 0         #  при отсутствии х коэфициент   становится = 0
        X1 = 0                      # исправляем положение чтобы не повредить строку при обрезке
    else:
        Stepen_in_Str1 = Get_Stepen(str1, X1)               # получаем степень х в str1 тип int
        Coefficient_in_Str1 = Get_Coefficient(str1, X1)     # получаем коэфициент х в str1  тип int

    if X2 == -1:                    # при переборе в str2 х не обнаружено срабатывает первый операнд выхода из цикла
        Cicle2_end = True
        Stepen_in_Str2 = 0            #  при отсутствии х степень   становится = 0
        Coefficient_in_Str2 = 0         #  при отсутствии х коэфициент   становится = 0
        X2 = 0                           # исправляем положение чтобы не повредить строку при обрезке
    else:
        Stepen_in_Str2 = Get_Stepen(str2, X2)                   # получаем степень х в str2  тип int
        Coefficient_in_Str2 = Get_Coefficient(str2, X2)         # получаем коэфициент х в str2  тип int

    if Cicle1_end and Cicle2_end : break

    if (Stepen_in_Str1 == Stepen_in_Str2):   # Проводим анализ степеней двух х из str1 и str2 если они равны (но не 0) проводим суммирование этих переменных 
        Coefficient = Coefficient_in_Str1 + Coefficient_in_Str2        # складываем коэфициенты двух х из str1 и str2
        
        if New_STRING !='': Plus = ' + '   # если в новой строке вводимый в нее новай х не первый то перед ним ставим знак +
        
        if Stepen_in_Str1 == 1:         # Проверка если степень х равна 1 то прибавляемый операнд степени х в новую строку ниему не равен ('4*х')
            Stepen_in_NewSTR = ''
        else: 
            Stepen_in_NewSTR = '^' + str(Stepen_in_Str1)          # степень х больше 1 то прибавляемый операнд степени х в новую строку  равен ('4*х^3')
        New_STRING = New_STRING + Plus + str(Coefficient) + '*x' + Stepen_in_NewSTR # добавляем в строку полученную сумму степеней х из str1 и str2


        str1 = Obrezka_strok(str1,X1,Stepen_in_Str1)                    # str1 = '6*x^3 + 4*x^2 + x + 1 = 0' обрезаем 6*x^3 + 
        str2 = Obrezka_strok(str2,X2,Stepen_in_Str2)                    # str2 = '4*x^2 + x + 1 = 0' обрезаем 4*x^2 + 

    elif  Stepen_in_Str1 > Stepen_in_Str2 :             # Проводим анализ степеней двух х из str1 и str2 при этом первая больше второй
                
        if New_STRING !='': Plus = ' + '   # если в новой строке вводимый в нее новай х не первый то перед ним ставим знак +
        
        if Stepen_in_Str1 == 1:         # Проверка если степень х равна 1 то прибавляемый операнд степени х в новую строку ниему не равен ('4*х')
            Stepen_in_NewSTR = ''
        else: 
            Stepen_in_NewSTR = '^' + str(Stepen_in_Str1)          # степень х больше 1 то прибавляемый операнд степени х в новую строку  равен ('4*х^3')
        if Coefficient_in_Str1 == 1:
            Coefficient = ''
        else:
            Coefficient = str(Coefficient_in_Str1) + '*'

        New_STRING = New_STRING + Plus + Coefficient + 'x' + Stepen_in_NewSTR      # добавляем в строку полученную сумму степеней х из str1 и str2

        str1 = Obrezka_strok(str1,X1,Stepen_in_Str1)                     # str1 = '6*x^3 + 4*x^2 + x + 1 = 0' обрезаем '6*x^3 +' 

    else:                                               # Исключение анализа  степень во второй строке больше чем степень в первой
                
        if New_STRING !='': Plus = ' + '   # если в новой строке вводимый в нее новай х не первый то перед ним ставим знак +
        
        if Stepen_in_Str2 == 1:         # Проверка если степень х равна 1 то прибавляемый операнд степени х в новую строку ниему не равен ('4*х')
            Stepen_in_NewSTR = ''
        else: 
            Stepen_in_NewSTR = '^' + str(Stepen_in_Str2)          # степень х больше 1 то прибавляемый операнд степени х в новую строку  равен ^3 ('4*х^3')
        
        if Coefficient_in_Str2 == 1:
            Coefficient = ''
        else:
            Coefficient = str(Coefficient_in_Str2) + '*'

        New_STRING = New_STRING + Plus + Coefficient + 'x' + Stepen_in_NewSTR # добавляем в строку полученную сумму степеней х из str1 и str2


        str2 = Obrezka_strok(str2,X2,Stepen_in_Str2)                     # str1 = '6*x^3 + 4*x^2 + x + 1 = 0' обрезаем '6*x^3 +' 

# Обрезка строк по х закончена 
# После обрезки по х должны остаться строки типа '= 0' (при коэфф = 0) или '5 = 0' (при коэфф = 5)
print(str1)
print(str2)
if Get_Coefficient_X0(str1) == 0 and Get_Coefficient_X0(str2) == 0:     # Проверка коэфициентов оставшихся строк(чтобы избежать появления "х + 0 = 0") 
    New_STRING = New_STRING + ' = 0'
else: 
    New_STRING = New_STRING + ' + ' + str(Get_Coefficient_X0(str1) + Get_Coefficient_X0(str2)) + ' = 0'  # сумирование коэфициентов (если хоть 1 не равен 0)


print('Данные уровнения просуммированы между собой:')
print(New_STRING)
print('И записаны в файл : Сумма многочленов.txt')
with open('Сумма многочленов.txt','w') as f:
    f.write(New_STRING)