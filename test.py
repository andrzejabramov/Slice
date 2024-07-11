# def create_islice_dict():
#     return start()
#
# def yes_no():
#     yn = input().upper()
#     if yn == 'N':
#         return start()
#     elif yn == 'Y':
#         return yn
#     else:
#         return f"Вы ввели неверное значение {yn} вместо Y или N, пожалуйста, повторите ввод: {yes_no()}"
#
# def start():
#     d = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3', 'key4': 'val4', 'key5': 'val5', 'key6': 'val6'}
#     l = len(d)
#     try:
#         txt = input(f"Обрезка словаря:\n{d}\nВведите начальный индекс обрезки a = ")
#         a = int(txt)
#         if a > l:
#             print(f"Вы ввели параметр start {a}, превышающий число пар словаря {l}. Это не приведет к ошибке," \
#                   f"но Вы получите пустой словарь,\nпоэтому мы поправили Вас и присвоили значению start " \
#                   f"значение длины словаря {l}.\nЕсли Вы согласны, введите Y, если нет введите N: ")
#             yes_no()
#             a_start = l
#         else:
#             a_start = a
#     except Exception:
#         print(f"Параметр start должно быть числом, Вы ввели недопустимый формат: {txt},\n" \
#               f"Повторите пожалуста ввод: ")
#         a_start = start()
#     return a_start
#
#
#
# print(start())
#
#
# def game(phrase_to_guess):
#     return input("Guess the phrase: ") == phrase_to_guess
#
# def main():
#     phrase = "hello, world"
#     while not game(phrase):
#         print("Incorrect.")
#     print("Correct")
#
# main()
#
#
#
import re


def input_param(descript):
    ins = input(descript)
    return ins

def param(d):
    l = len(d)
    note_start = f"Обрезка словаря:\n{d}\nВведите начальный индекс обрезки a = "
    note_err = f"Параметр должно быть числом, Вы ввели недопустимый формат,\n" \
              f"Повторите пожалуста ввод: "
    regex = r'\D'
    a = input_param(note_start)
    while len(re.findall(regex, a)) > 0:
        a = input_param(note_err)
    a = int(a)
    note = f"Вы ввели параметр start {a}, превышающий число пар словаря {l}. Это не приведет к ошибке," \
           f"но Вы получите пустой словарь,\nпоэтому мы поправили Вас и присвоили значению start " \
           f"значение длины словаря {l}.\nЕсли Вы согласны, введите Y, если нет введите N: "
    note_yn = f"Вы ввели неверное значение вместо Y или N, пожалуйста, повторите ввод: "
    start_param = 'start'
    if a > l:
        yn = input_param(note).upper()
        while yn != 'Y' and yn != 'N':
            yn = input_param(note_yn).upper()
        if yn == 'N':
            param()
        elif yn == 'Y':
            a_start = l
            return a_start
    else:
        a_start = a
        note_stop = 'введите конечный индекс обрезки, помните, что он не включается в выборку: b = '
        b = input_param(note_stop)
        regex = r'\D'
        if len(re.findall(regex, b)) == 0:
            note_ab = f"Вы ввели параметр stop {b} меньше, чем параметр start {a_start}, это не приведет к ошибке," \
                      f"но Вы получите пустой словарь,\nпоэтому мы поправили Вас и присвоили значению stop " \
                      f"значение параметра start {a_start}.\nЕсли Вы согласны, введите Y, если нет введите N: "
            if b < a_start:
                print(note_ab)
                input_param(note)
                b_stop = a_start
                return b_stop
            elif b > l:
                print(f"Вы ввели параметр stop {b} превышающий число пар словаря {l}. Это не приведет к ошибке,"
                      f"но Вы получите пустой словарь,\nпоэтому мы поправили Вас и присвоили значению stop " \
                      f"значение значение длины словаря {l}.\nЕсли Вы согласны, введите Y, если нет введите N: ")
                yes_no()
                b_stop = l
                return b_stop
            print(f"Параметр start должно быть числом, Вы ввели недопустимый формат: {txt},\n" \
                  f"Повторите пожалуста ввод: ")
            b_stop = input_param(note_stop)
        elif b == 'None':
            b_stop = None
        else:
            b_stop = 'alarm'
        return b_stop
#---------------------------------------

d = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3', 'key4': 'val4', 'key5': 'val5', 'key6': 'val6'}
print(param(d))