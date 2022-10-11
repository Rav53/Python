
# Задача №38: Создайте программу для игры с конфетами человек против человека. 
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# б) Подумайте, как наделить бота "интеллектом"

import os
from random import randint
os.system('cls' if os.name == 'nt' else 'clear')

def NextPlayerStep():
    Cicle = True
    while Cicle:            
        str1 = input('Сколько конфет вы возьмете.  Ваш выбор-')         # Запрос кол-ва конфет
        try:
            Number = int(str1)
            if Number > 28 or Number < 1:    # проверка на погрешность   1 < Number < 28
                print('Введите число больше 0, но не более 28   ')
            else:
                Cicle = False       # Введенное число подходит - выходим из цикла
        except ValueError:
            print("Это не правильный ввод. Введите число больше 0, но не более 28") 
    return   Number 


def NextBotStep(kycha,livel,poridok_hodov):         
    if livel == '1':                        # Расчет ходов осуществяется по теории победного хода
        if kycha <= 28:
            print(f'Компьютер берет  - {kycha} конфет') 
            return kycha
                               # Если poridok_hodov = 0 бот ходит первым (необходимо для победного алгоритма)
        if kycha > 57:
            if kycha % 28 == 0:
                hand_bot = 27
            else:
               hand_bot = kycha % 28 - 1 
        else:
            hand_bot = kycha - 29
        print(f'Компьютер берет  - {hand_bot} конфет')
        return hand_bot
    else:                                       
        if kycha <= 28:
            print(f'Компьютер берет  - {kycha} конфет')
            return kycha
        hand_bot = randint(1,28)                # генератор случайных ходов для тупенького бота
        print(f'Компьютер берет  - {hand_bot} конфет')
        return hand_bot


    # ТИПА ИНТЕРФЕЙС
print('                                                 ИГРА КУЧА КОНФЕТ')
print('         Правила игры:  На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.  ')
print('Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет (1 конфета минимум). ')
print('                                 Все конфеты оппонента достаются сделавшему последний ход. ')
print(' ')
print('                                         Внимание игра начинается !!!!')
print(' ')
print(' ')


complexity = 1

Kucha = 100
poriadok_hodov = randint(0,1)
if poriadok_hodov == 1:
    print(f'                                    Вы делаете первый ход!')  
else:     
    print(f'                                        Вы ходите вторым!')

print(f'На столе на начало игры {Kucha} конфет')

PlayerWIN = False   
ENDGAME = False
Step_of_game = 1
while not(ENDGAME):
    if poriadok_hodov == 1:     # Игрок ходит первым
        Kucha -= NextPlayerStep()
        if Kucha <= 0: 
            ENDGAME = True
            PlayerWIN = True
            break
        print(f'На столе осталось {Kucha} конфет')
        Kucha -= NextBotStep(Kucha,complexity,poriadok_hodov)
        if Kucha <= 0: 
            ENDGAME = True
            PlayerWIN = False
        print(f'На столе осталось {Kucha} конфет')
        print()
    else:
        Kucha -= NextBotStep(Kucha,complexity,poriadok_hodov)
        if Kucha <= 0: 
            ENDGAME = True
            PlayerWIN = False
            break
        print(f'На столе осталось {Kucha} конфет')
        Kucha -= NextPlayerStep()
        if Kucha <= 0: 
            ENDGAME = True
            PlayerWIN = True
        print(f'На столе осталось {Kucha} конфет')
        print()
if PlayerWIN:
    print('ПОЗДРАВЛЯЮ ВЫ ПОБЕДИЛИ')
else:
    if complexity == '1':
        print('ПРОИГРЫШ!!! Это было неизбежно на ТАКОМ уровне сложности)))) ')
    else:
        print('ПРОИГРЫШ!!! Это печально на ТАКОМ уровне сложности)))) ')