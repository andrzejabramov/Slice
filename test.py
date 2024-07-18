import re

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

notify = 'jhgjh'
min_param = 1
val_param = 'stop'
f_note = '765765765 '
l = 6

def input_param(notify):
    ins = input(notify)
    return ins

def valid_ins(min_param, val_param, l, f_note):
    txt = input_param(f_note)
    while True:
        try:
            ans = int(txt)
            if ans < min_param:
                while True:
                    print(f"Параметр {val_param} должно быть None или больше или равно {min_param}. "
                          f"Введите пожалуйста корректное значение: ")
                    ans = valid_ins(min_param, val_param, l, f_note)
                    break
            elif ans > l:
                note_param = f"Вы ввели параметр stop {val_param} {ans} превышающий число пар словаря {l}.\n" \
                             f"Это не приведет к ошибке, но Вы получите пустой словарь,\n" \
                             f"поэтому мы поправили Вас и присвоили значению {val_param} " \
                             f"значение значение длины словаря {l}.\nЕсли Вы согласны, введите Y, если нет введите N: "
                note_yn = None
                yn = input_param(note_param).upper()
                while yn != 'Y' and yn != 'N':
                    yn = input_param(note_yn).upper()
                if yn == 'Y':
                    ans = l
                else:
                    exit
            break
        except Exception:
            if txt == 'None':
                ans = None
                break
            else:
                print(f"Параметр {val_param} должно быть числом или None,\n"
                      f"Вы ввели недопустимый формат: {txt},\n" \
                      f"Повторите пожалуста ввод: ")
                txt = input_param(f_note)
    return ans

print(valid_ins(min_param, val_param, l, f_note))
