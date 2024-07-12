from itertools import islice

descript = 'Выберите цифру для просмотра метода словарей:\n'
'1 создания словаря с помощью литерала\n'
'2 создания словаря с помощью функции dict\n'
'3 создания словаря с помощью метода fromkeys (значения ключей по умолчанию)\n'
'4 создания словаря с помощью архива zip\n'
'5 создания словаря с помощью генераторов словарей\n'
'6 создание словаря методом копирования copy()'
'7 получение значений из словаря по ключу\n'
'8 получение значения None (исключение ошибки) по несуществующему ключу методом get()\n'
'9 получение списка ключей словаря\n'
'10 получение списка значений словаря\n'
'11 получение списка кортежей ключ-значение\n'
'12 получение различных элементов словаря при помощи итерации\n'
'13 сортировка элементов словаря\n'
'14 обрезка словаря\n'

class Dict_list:
    def __init__(self, ins):
        self.ins = ins

    def input_data(self, ins):
        inp = input(descript)
        match inp:
            case '1':
                return self.create_literal(ins)
            case '2':
                return self.create_fdict()
            case '3':
                return self.create_fromkeys()
            case '4':
                return self.create_zip()
            case '5':
                return self.create_comprehension()
            case '6':
                return self.create_copy(ins)
            case '7':
                return self.create_getdata(ins)
            case '8':
                return self.create_get_dict(ins, note='Введите несуществующий ключ для проверки метода get()')
            case '9':
                return self.create_key_dict(ins)
            case '10':
                return self.create_val_dict(ins)
            case '11':
                return self.create_items_dict(ins)
            case '12':
                return self.create_iter_dict(ins)
            case '13':
                return self.create_sort_dict(ins)
            case '14':
                return self.create_islice_dict()
            case _:
                print('Вы ввели номер несуществующего метода, попробуйте еще раз:')
                return self.input_data()

    def create_literal(self, ins):#1
        return 'создания словаря с помощью литерала\nd = {}\nd = ' + f"{ins}"

    def create_fdict(self):#2
        d = dict(key1='val1', key2=2, key3=False)
        return f"создания словаря с помощью функции dict\nd = dict(key1=\'val1\', key2=2, key3=False)\nprint(d)\n{d}"

    def create_fromkeys(self):#3
        d = dict.fromkeys(['key1', 'key2'], 'val')
        return f"создания словаря с помощью метода fromkeys\nd = dict.fromkeys([\'key1\', \'key2\'], \'val\')\nprint(d)\n{d}"

    def create_zip(self):#4
        key_list = ['key1', 'key2', 'key3']
        val_list = ['val', 1, True]
        result_dict = dict(zip(key_list, val_list))
        return f"создания словаря с помощью архива zip\nkey_list = [\'key1\', \'key2\', \'key3\']\n" \
        f"val_list = [\'val\', 1, True]\n" \
        f"result_dict = dict(zip(key_list, val_list))\n" \
        f"print(result_dict)\n{result_dict}"

    def create_comprehension(self):#5
        d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        d1 = {k: v * 2 for (k, v) in d.items()}
        return f"создания словаря с помощью генераторов словарей\nd = {d}\n" + 'd1 = {k: v * 2 for (k, v) in d.items()}\n' + f"print(d1)\n{d1}"

    def create_copy(self, ins):#6
        id_d = id(ins)
        d_copy = ins.copy()
        id_d_copy = id(d_copy)
        return f"создания словаря копированием.\nИсходный словарь: d = {ins}\n" \
               f"Eго id в памяти:\nid_d = id(d)\n{id_d}\nНовый экземпляр словаря, скопированный из исходного:\n" \
               f"d_copy = d.copy()\n{d_copy}.\n" \
               f"Его id в памяти:\nid_d_copy = id(d_copy)\n{id_d_copy}\nотличается от исходного"

    #7
    def create_getdata(self, ins, note='указанный ключ отсутствует в словаре. Для устранения ошибки используйте метод get()'):
        key = input(f"Получение значения из словаря по ключу.\n"
                    f"Введите ключ для получения значения из словаря\nd = {ins}: \n")
        try:
            res = ins[key]
            return res
        except Exception:
            return note

    def create_get_dict(self, ins, note):#8
        key = input('Исключение ошибки при вводе несуществующего ключа методом get()\n'
                    ''+note+f"для словаря:\n{ins}: \n")
        res = ins.get(key)
        if res is None:
            return res
        else:
            note = 'Вы ввели существующий ключ, введите пожалуйста не существующий: '
            return self.create_get_dict(ins, note)

    def create_key_dict(self, ins):#9
        res = ins.keys()
        return f"получение списка ключей словаря:\nd = {ins}\nres = d.keys()\nres = {res}"

    def create_val_dict(self, ins):#10
        res = ins.values()
        return f"получение списка значений словаря:\nd = {ins}\nres = d.values()\nres = {res}"

    def create_items_dict(self, ins):#11
        res = ins.items()
        return f"получение списка кортежей ключ-значение словаря:\nd = {ins}\nres = d.items()\nres = {res}"

    def create_iter_dict(self, ins):#12
        print(f"итерируем словарь по ключам:\nd = {ins}\nfor key in d:\n    print(key)")
        for key in ins:
            print(key)
        print(f"итерируем словарь по парам ключ-значение:\nd = {ins}\nfor key, value in d.items():\n    print(key, value)")
        for key, value in ins.items():
            print(key, value)
        return ''

    def create_sort_dict(self, ins):#13
        try:
            d_sort_key = dict(sorted(ins.items()))
            print(f"сортировка словаря:\n{ins}\nпо ключам:\nd_sort_key = dict(sorted(d.items()))\n{d_sort_key}")
            d_sort_val = dict(sorted(ins.items(), key=lambda item: item[1]))
            print(f"сортировка этого же словаря по значениям:\n"
                  f"d_sort_val = dict(sorted(d.items(), key=lambda item: item[1]))\n{d_sort_val}")
        except Exception:
            print(f"Сортировка словаря: \n{ins}\nзавершилась ошибкой, которая, вероятно, вызвана тем, "
                  f"что в ключах и/или значениях есть формат int и str.\n"
                  f"Приведите ключи между собой и значения к единому формату\n"
                  f"(формат ключей может отличаться от формата значений) и попробуйте снова, например: ")
            ins = {'key3': 1, 'key2': 3, 'key1': 5, 'key4': 4, 'key5': 2, 'key6': 6}
            return self.create_sort_dict(ins)
        return ''

    def create_islice_dict(self):#14
        return self._param()

    def _input_param(self, notify):
        ins = input(notify)
        return ins

    def _param(self):
        ins_dict = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3', 'key4': 'val4', 'key5': 'val5', 'key6': 'val6'}
        note_dict = f"Введите произвольный словарь, например,\nскопируйте и введите предложенный вариант:\n{ins_dict}\n"
        d = self._input_param(notify=note_dict)
        while True:
            try:
                d = eval(d)
                l = len(d)
                break
            except Exception:
                print('Вы ввели неверный формат словря, пожалуйста, повторите ввод правильно: ')
                d = self._input_param(notify=note_dict)

        note_start = f"Обрезка словаря:\n{d}\nВведите начальный индекс обрезки a = "
        txt = self._input_param(note_start)
        while True:
            try:
                a = int(txt)
                break
            except Exception:
                print(f"Параметр start должно быть числом, Вы ввели недопустимый формат: {txt},\n" \
                      f"Повторите пожалуста ввод: ")
                txt = self._input_param(note_start)
        while a > l:
            note_a = f"Вы ввели параметр start {a}, превышающий число пар словаря {l}. Это не приведет к ошибке," \
                     f"но Вы получите пустой словарь,\nпоэтому мы поправили Вас и присвоили значению start " \
                     f"значение длины словаря {l}.\nЕсли Вы согласны, введите Y, если нет введите N: "
            note_yn = f"Вы ввели неверное значение вместо Y или N, пожалуйста, повторите ввод: "
            yn = self._input_param(note_a).upper()
            while yn != 'Y' and yn != 'N':
                yn = input_param(note_yn).upper()
            if yn == 'N':
                self._param()
            else:
                a = l
        else:
            a_start = a

        # note_stop = 'введите конечный индекс обрезки, помните, что он не включается в выборку: b = '
        # try:
        #     txt = self._input_param(note_stop)
        #     b = int(txt)
        #     if b < a:
        #         print(f"Вы ввели параметр stop {b} меньше, чем параметр start {a}, это не приведет к ошибке," \
        #               f"но Вы получите пустой словарь,\nпоэтому мы поправили Вас и присвоили значению stop " \
        #               f"значение параметра start {a}.\nЕсли Вы согласны, введите Y, если нет введите N: ")
        #         self._yes_no()
        #         b_stop = a
        #     elif b > l:
        #         print(f"Вы ввели параметр stop {b} превышающий число пар словаря {l}. Это не приведет к ошибке,"
        #               f"но Вы получите пустой словарь,\nпоэтому мы поправили Вас и присвоили значению stop " \
        #               f"значение значение длины словаря {l}.\nЕсли Вы согласны, введите Y, если нет введите N: ")
        #         self._yes_no()
        #         b_stop = l
        # except Exception:
        #     print(f"Параметр start должно быть числом, Вы ввели недопустимый формат: {txt},\n" \
        #           f"Повторите пожалуста ввод: ")
        #     b_stop = self._input_param(note_stop)

        # c = input('введите шаг выборки с = ')
        # def islice_dict(a_start=0, b_stop=0, c_step=None):
        #     d_islice = dict(islice(d.items(), a_start, b_stop, c_step))
        #     return d_islice
        # try:
        #     c = int(c)
        #     res = islice_dict(a, b, c)
        # except:
        #     c = None
        #     return f"Вы ввели неверный параметр step, который может принимать значения " \
        #            f"либо None либо целое число более 0, поэтому введенное Вами значение преобразовано в None\n" \
        #            f"d_islice = dict(islice(d.items(), {a}, {b}, {c}))\n{islice_dict(a, b, c)}"
        return a_start #+ ' ' + b_stop)