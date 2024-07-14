from itertools import islice

descript = 'Выберите цифру для просмотра метода словарей:\n' \
'1 создания словаря с помощью литерала\n' \
'2 создания словаря с помощью функции dict\n' \
'3 создания словаря с помощью метода fromkeys (значения ключей по умолчанию)\n' \
'4 создания словаря с помощью архива zip\n' \
'5 создания словаря с помощью генераторов словарей\n' \
'6 создание словаря методом копирования copy()' \
'7 получение значений из словаря по ключу\n' \
'8 получение значения None (исключение ошибки) по несуществующему ключу методом get()\n' \
'9 получение списка ключей словаря\n' \
'10 получение списка значений словаря\n' \
'11 получение списка кортежей ключ-значение\n' \
'12 получение различных элементов словаря при помощи итерации\n' \
'13 сортировка элементов словаря\n' \
'14 обрезка словаря\n' \
'15 добавление в словарь пары ключ-значение\n' \
'16 обновление словаря методом update\n' \
'17 чтение и/или добавление пары ключ-значение методом setdefault()\n' \
'18 удаление пары ключ-значение из словаря методом del()\n' \
'19 очищение словаря от всех данных методом clear()\n' \
'20 удаление и получение удаленной пары ключ-значение словаря методом pop()\n' \
'21 удаление и получение последней пары ключ-значение словаря методом popitem()\n' \
'22 получение списка из словаря\n' \
'23 применение метода dir() словаря\n'

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
                return self.create_islice_dict(ins)
            case '15':
                return self.create_insert_dict(ins)
            case '16':
                return self.create_update_dict(ins)
            case '17':
                return self.create_setdefault_dict(ins)
            case '18':
                return self.create_del_dict(ins)
            case '19':
                return self.create_clear_dict(ins)
            case '20':
                return self.create_pop_dict(ins)
            case '21':
                return self.create_popitem_dict(ins)
            case '22':
                return self.create_list_dict(ins)
            case '23':
                return self.create_dir_dict(ins)
            case _:
                print('Вы ввели номер несуществующего метода, попробуйте еще раз:')
                return self.input_data(ins)

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
            if type(key) == float:
                key = float(key)
            res = ins[key]
            return f"val = d[{key}]\n{res}"
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

    def create_islice_dict(self, ins):#14
        return self._param(ins)

    def _input_param(self, notify):
        ins = input(notify)
        return ins

    def _valid_ins(self, min_param, val_param, l, f_note):
        txt = self._input_param(f_note)
        if txt == 'None':
            ans = None
        else:
            while True:
                try:
                    ans = int(txt)
                    break
                except Exception:
                    print(f"Параметр {val_param} должно быть числом или None,\n"
                          f"Вы ввели недопустимый формат: {txt},\n" \
                          f"Повторите пожалуста ввод: ")
                    txt = self._input_param(f_note)
            while ans < min_param:
                print(f"Параметр {val_param} должно быть None или больше или равно {min_param}. "
                      f"Введите пожалуйста корректное значение: ")
                {self._input_param(f_note)}
            if ans > l:
                note_param = f"Вы ввели параметр stop {val_param} {ans} превышающий число пар словаря {l}.\n" \
                             f"Это не приведет к ошибке, но Вы получите пустой словарь,\n" \
                             f"поэтому мы поправили Вас и присвоили значению {val_param} " \
                             f"значение значение длины словаря {l}.\nЕсли Вы согласны, введите Y, если нет введите N: "
                note_yn = None
                yn = self._input_param(note_param).upper()
                while yn != 'Y' and yn != 'N':
                    yn = self.input_param(note_yn).upper()
                if yn == 'Y':
                    ans = l
        return ans

    def _param(self, ins):
        note_dict = f"Обрезка словаря. Введите произвольный словарь, например,\nскопируйте и введите предложенный вариант:\n{ins}\n" \
                    f"Предупреждение!!! При копировании предложенного варианта словаря из блока Run pycharm\n" \
                    f"блок переводится в режим чтения без возможности обратного переключения\n" \
                    f"и после ввода скопированой строки дальнейший ввод данных в блоке Run невозможен.\n" \
                    f"Для восстановления работоспособности после копирования словаря в память перезапустите этот тест\n"
        min_param = 0
        val_param = 'start'
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
        a_start = self._valid_ins(min_param, val_param, l, note_start)
        note_stop = 'введите конечный индекс обрезки, помните, что он не включается в выборку: b = '
        val_param = 'stop'
        b_stop = self._valid_ins(min_param, val_param, l, note_stop)
        if b_stop < a_start:
            note_b = f"Вы ввели параметр {val_param} {b_stop} меньше, чем параметр start {a_start},\n" \
                     f"это не приведет к ошибке, но Вы получите пустой словарь,\n" \
                     f"поэтому мы поправили Вас и присвоили значению {val_param} " \
                     f"значение параметра start {a_start}.\nЕсли Вы согласны, введите Y, если нет введите N: "
            note_yn = None
            yn = self._input_param(note_b).upper()
            while yn != 'Y' and yn != 'N':
                yn = self.input_param(note_yn).upper()
            if yn == 'Y':
                b_stop = a_start
        note_step = 'введите шаг выборки: с= '
        val_param = 'step'
        min_param = 1
        c_step = self._valid_ins(min_param, val_param, l, note_step)
        res = dict(islice(d.items(), a_start, b_stop, c_step))
        return f"Результат выполнения теста:\nd = {ins}\n" \
               f"res = dict(islice(d.items(), {a_start}, {b_stop}, 1))\n{res}"

    def create_insert_dict(self, ins):#15
        pass
    def create_update_dict(self, ins):#16
        pass

    def create_setdefault_dict(self, ins):#17
        pass

    def create_del_dict(self, ins):#18
        pass

    def create_claer_dict(self, ins):#19
        pass

    def create_pop_dict(self, ins):#20
        pass

    def create_popitem_dict(self, ins):#21
        pass

    def create_list_dict(self, ins):#22
        pass

    def create_dir_dict(self, ins):#23
        pass
