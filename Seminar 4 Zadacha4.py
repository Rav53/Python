# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Пример
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1


def func_find(list, find_str):
    if list.count(find_str) > 1:
        a = list.index(find_str)
        print(list.index(find_str, a + len(find_str)))
    else:
        print(-1)


list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
f = "qwe"
func_find(list, f)
list = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
f = "йцу"
func_find(list, f)
list = ["йцу", "фыв", "ячс", "цук", "йцукен"]
f = "йцу"
func_find(list, f)
list = ["123", "234", 123, "567"]
f = "123"
func_find(list, f)
list = []
f = "123"
func_find(list, f)