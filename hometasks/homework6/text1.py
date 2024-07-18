from itertools import islice


d = {1: 'val1', 'key2': 2, 'key3': True, 'key4': [('o', 1), ('p', 2), ('q', 3)], 'key5': {'key': 'val'}, 'key6': None}
l1 = len(d)
notify = 'notify'
val_param1 = 'stop'
f_note = 'Введите значение: '
note_yn = None
min_param1 = 0

def input_param(notify):
    ins = input(notify)
    return ins

def valid_ins(min_param, val_param, l, f_note):
    txt = input_param(f_note)
    while True:
        try:
            ans = int(txt)
            if ans < min_param:
                while ans < min_param:
                    print(f"Параметр {val_param} должно быть None или больше или равно {min_param}. "
                         f"Введите пожалуйста корректное значение: ")
                    input_param(f_note)
            if ans > l:
                note_param = f"Вы ввели параметр {val_param} {ans} превышающий число пар словаря {l}.\n" \
                             f"Это не приведет к ошибке, но Вы получите пустой словарь,\n" \
                             f"поэтому мы поправили Вас и присвоили значению {val_param} " \
                             f"значение длины словаря {l}.\nЕсли Вы согласны, введите Y, если нет введите N: "
                yn = input_param(note_param).upper()
                while yn != 'Y' and yn != 'N':
                    yn = input_param(note_yn).upper()
                if yn == 'Y':
                    ans = l
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

print(valid_ins(min_param1, val_param1, l1, f_note))
