def Riper(count):
    if count > 9 and count < 100:   # При совпадениях больше 10 но меньше 100 ставим (рипер *) перед счетчиком
        return '*'
    elif count > 100:           # При совпадениях больше 100 ставим (рипер **) перед счетчиком (совпадения более 1000 не рассматриваем)
        return '**'
    else:
        return ''
def RLE_coder(text): 
    encoding = ''       # Последовательность после кодирования
    prev_char = ''      # Предыдущий символ
    count = 1 
    if not text:        # Если на входе пусто возвращаем пустую строку
        return '' 
    for char in text:           #   Перебираем все символы в строке
        if char != prev_char:       # Если символ не равен предыдущему
            if prev_char:           #  И если предыдущий не ''
                encoding += Riper(count) + str(count) + prev_char  # вносим данные
            count = 1 
            prev_char = char 
        else:  
            count += 1 
            # добавляем последний элемент
    encoding += Riper(count) + str(count) + prev_char  # вносим данные 
    return encoding

List = []


with open('NOTCODINGTEXT.txt','r',encoding='utf-8') as f:         # Открываем файл для чтения
    List = [line.rstrip() for line in f]                    # считываем из файловой переменной строку (автоматически обрезаем '\n' в конце строки) и записываем в список

CODINGList = []                         
for Line in List:
    CODINGList.append(RLE_coder(Line))          # Производим сжатие данных по RLE алгоритму (простейшему, если повторениу нет то обьем данных вырастет вдвое)




NewENCODINGList = []
for Line in CODINGList:
    NewENCODINGList.append(Line + '\n')         # создаем новый список строк и добавляем переносы строк для коректной записи в файл

with open('CODINGTEXT.txt','w',encoding='utf-8') as f:         # Открываем файл для записи
    f.writelines(NewENCODINGList)                               # Производим запись в файл

# МОДУЛЬ ДЕКОДИРОВЩИКА

def RLE_Decoding(TEXT):                     #  *21r*11t1v1f1g1s751e1r3d956m1e = rrrrrrrrrrrrrrrrrrrrrtttttttttttvfgs5555555erddd555555555mmmmmme
    Pixel10 = False           # рипер на 10 повторений
    Pixel100 = False          # рипер на 100 повторений
    Pixel = False             # рипер на 1-9 повторений
    Decoding = ''
    Count = 0
    Count_of_Char = ''
    
    if not TEXT:                       # Если на входе пусто возвращаем пустую строку
        return ''
    for char in TEXT:
        
        if char =='*':                   # если символ - рипер и Pixel10 = False то 
            if not Pixel10: 
                Pixel10 = True
            else:
                Pixel100 = True
                Pixel10 = False           
        else:
            if Pixel10:              # если символ - рипер и Pixel10 = False то
                if Count < 2:
                    Count += 1
                    Count_of_Char += char
                else :
                    Decoding += char * int(Count_of_Char)
                    Pixel100 = False
                    Pixel10 = False
                    Count = 0
                    Count_of_Char =''
            elif Pixel100:
                if Count < 3:
                    Count += 1
                    Count_of_Char += char
                else :
                    if not Count_of_Char:
                        Decoding += char * int(Count_of_Char)
                        Pixel100 = False
                        Pixel10 = False
                        Count = 0
                        Count_of_Char =''
            else:
                if not Pixel:
                    Count_of_Char = char
                    Pixel = True
                else:
                    Decoding += char * int(Count_of_Char)
                    Pixel = False
                    Count_of_Char = ''
    
    return Decoding
List = []
with open('CODINGTEXT.txt','r',encoding='utf-8') as f:         # Открываем файл для чтения
    List = [line.rstrip() for line in f]                    # считываем из файловой переменной строку (автоматически обрезаем '\n' в конце строки) и записываем в список

CODINGList = []                         
for Line in List:
    CODINGList.append(RLE_Decoding(Line))          # Производим сжатие данных по RLE алгоритму (простейшему, если повторениу нет то обьем данных вырастет вдвое)




NewENCODINGList = []
for Line in CODINGList:
    NewENCODINGList.append(Line + '\n')         # создаем новый список строк и добавляем переносы строк для коректной записи в файл

with open('DECODINGTEXT.txt','w',encoding='utf-8') as f:         # Открываем файл для записи
    f.writelines(NewENCODINGList)                               # Производим запись в файл