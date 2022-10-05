# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#Всегда ли правдиво выражение? оно всегда должно быть верным.

for x in range(2):
       for y in range(2):
           for z in range(2):
               print(not (x or y or z) == (not x and not y and not z))
               print(x, y, z,)

#for x in range(2):
#    for y in range(2):
#        for z in range(2):
#            if not (x or y or z) == (not x and not y and not z):
#                print(f'For {x}, {y}, {z}:', True)
#            else:
#                print(False)


























