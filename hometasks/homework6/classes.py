from itertools import islice

descript = 'Выберите цифру для просмотра метода словарей:\n' \
'1 создания словаря с помощью литерала\n' \
'2 создания словаря с помощью функции dict\n' \
'3 создания словаря с помощью метода fromkeys (значения ключей по умолчанию)\n' \
'4 создания словаря с помощью архива zip\n' \
'5 создания словаря с помощью генераторов словарей\n' \
'6 создание словаря методом копирования copy()\n' \
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
'20 удаление пары ключ-значение и получение удаленного значения словаря методом pop()\n' \
'21 удаление и получение последней пары ключ-значение словаря методом popitem()\n' \
'22 получение длины словаря\n' \
'23 применение метода dir() словаря\n' \
'24 создание множества вручную\n' \
'25 создвние множества из списка методом set()\n' \
'26 создание пустого множества\n' \
'27 доступ к элементам множества с помощью цикла\n' \
'28 проверка принадлежности элемента множеству\n' \
'29 добавление элемента множества\n' \
'30 удаление элементов множества методом discard()\n' \
'31 удаление элементов множества методом remove()\n' \
'32 удаление элементов множесива и возврат удаленных/оставшихся методом pop()\n' \
'33 удаление элементов множества методом clear()\n' \
'34 объединение множеств методом union()\n' \
'35 пересечение множеств методом intersection() или &\n' \
'36 определение является ли множество пересечением методом isdisjoint()\n' \
'37 определение разницы множеств методами difference() и symmetric_difference()\n' \
'38 сравнене множеств\n' \
'39 копирование множеств методом copy()\n' \
'40 определение длины множества методом len()\n' \
'41 замороженное множество с помощью метода frozenset()\n' \
'42 иные функции множеств\n'

class Dict_list:
    def __init__(self, ins, lmethod, descript):
        self.ins = ins
        self.lmethod = lmethod
        self.descript = descript

    def descr(self):
        return descript

    def valid_metod(self, lmethod, descript):
        method_list = []
        for row in descript:
            if row == '\n':
                st = descript.find('\n') + 1
                descript = descript[st:]
                en = descript.find(' ')
                sub_l = descript[:en]
                if sub_l != '':
                    method_list.append(sub_l)
        try:
            ans = True if method_list.index(lmethod) < 23 else False
        except Exception:
            ans = False
        return ans

    def input_data(self, lmethod, ins):
        match lmethod:
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
                return self.create_len_dict(ins)
            case '23':
                return self.create_dir_dict(ins)
            case '24':
                return self.create_hand_set(ins)
            case '25':
                return self.create_set_list(ins)
            case '26':
                return self.create_null_set(ins)
            case '27':
                return self.create_circle_set(ins)
            case '28':
                return self.create_in_set(ins)
            case '29':
                return self.create_add_set(ins)
            case '30':
                return self.create_discard_set(ins)
            case '31':
                return self.create_remove_set(ins)
            case '32':
                return self.create_pop_set(ins)
            case '33':
                return self.create_clear_set(ins)
            case '34':
                return self.create_union_set(ins)
            case '35':
                return self.create_intersection_set(ins)
            case '36':
                return self.create_isdisjoint_set(ins)
            case '37':
                return self.create_diff_set(ins)
            case '38':
                return self.create_compare_set(ins)
            case '39':
                return self.create_copy_set(ins)
            case '40':
                return self.create_len_set(ins)
            case '41':
                return self.create_frozenset_set(ins)
            case '42':
                return self.create_other_set(ins)
            case _:
                print('Вы ввели номер несуществующего метода, попробуйте еще раз:')
                return ''

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
        while True:
            try:
                ans = int(txt)
                if ans < min_param:
                    while True:
                        print(f"Параметр {val_param} должно быть None или больше или равно {min_param}. "
                              f"Введите пожалуйста корректное значение: ")
                        ans = self._valid_ins(min_param, val_param, l, f_note)
                        break
                elif ans > l:
                    note_param = f"Вы ввели параметр stop {val_param} {ans} превышающий число пар словаря {l}.\n" \
                                 f"Это не приведет к ошибке, но Вы получите пустой словарь,\n" \
                                 f"поэтому мы поправили Вас и присвоили значению {val_param} " \
                                 f"значение значение длины словаря {l}.\nЕсли Вы согласны, введите Y, если нет введите N: "
                    note_yn = None
                    yn = self._input_param(note_param).upper()
                    while yn != 'Y' and yn != 'N':
                        yn = self._input_param(note_yn).upper()
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
                    txt = self._input_param(f_note)
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
        if type(b_stop) == int and b_stop < a_start:
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
               f"res = dict(islice(d.items(), {a_start}, {b_stop}, {c_step}))\n{res}"

    def create_insert_dict(self, ins):#15
        ins1 = ins.copy()
        ins2 = ins.copy()
        ins1['key7'] = {'key8': 'val8'}
        ins2 = ins2.update(dict(key9='val9', key10=10))
        return f"добавление пары ключ значене вариант1 (одна пара):\n" \
               f"d = {ins}\nd['key7'] = {{'key8': 'val8'}}\nd = {ins1}"

    def create_update_dict(self, ins):#16
        ins1 = ins.copy()
        ins1.update({'key7': {'key8': 'val8'}})
        ins2 = ins1.copy()
        ins2.update({'key7': 'val7'})
        return f"обновление словаря или добавление пар ключ значение:\nd = {ins}\n" \
               f"добавление:\nd.update({{'key7: {{'key8': 'val8'}}}})\n{ins1}\n" \
               f"обновление:\nd.update({{'key7': 'val7'}})\n{ins2}"

    def create_setdefault_dict(self, ins):#17
        ins1 = ins.copy()
        ins1.setdefault('key2', 6)
        ins2 = ins.copy()
        ins2.setdefault('key7', {'key8': 'val8'})
        ins3 = ins.copy()
        ins3.setdefault('key9')
        return f"чтение и/или добавление пары ключ-значение методом setdefault():\n" \
               f"d = {ins}\nвыбираем существующий ключ, но с произвольным значением:\n" \
               f"d.setdefault('key1', 6)\n{ins1}\nвыбираем несуществующую пару ключ-значение: \n" \
               f"d.setdefault('key7', {{'key8': 'val8'}})\n{ins2}\nвыбираем несуществующий ключ без значения:\n{ins3}"

    def create_del_dict(self, ins):#18
        ins1 = ins.copy()
        del ins1['key2'], ins1['key6']
        return f"удаление пар ключ-значение из словаря методом del():\nd = {ins}\n" \
               f"del ins['key2'], ins['key6']\n{ins1}"

    def create_clear_dict(self, ins):#19
        ins1 = ins.copy()
        ins1.clear()
        return f"очищение словаря от всех данных методом clear():\nd = {ins}\n" \
               f"d.clear()\n{ins1}"

    def create_pop_dict(self, ins):#20
        ins1 = ins.copy()
        res = ins1.pop('key2')
        return f"удаление пары ключ-значение и получение удаленного значения словаря методом pop():\n" \
               f"d = {ins}\nres = d.pop('key2')\nзначение удаленной пары: {res}\n" \
               f"словарь с удаленной парой ключ-значение:\n{ins1}"


    def create_popitem_dict(self, ins):#21
        ins1 = ins.copy()
        res = ins1.popitem()
        return f"удаление и получение последней пары ключ-значение словаря методом popitem():\n" \
               f"d = {ins}\nres = d.popitem()\nметод вовращает кортеж из удаленных ключа и значения\n{res}\n" \
               f"словарь с удаленной последней парой ключ-значение:\n" \
               f"{ins1}\nПрименение этого метода к единствеенной паре словаря вызовет ошибку"

    def create_len_dict(self, ins):#22
        l = len(ins)
        return f"получение длины словаря:\nd = {ins}\nl = len(d)\n{l}"

    def create_dir_dict(self, ins):#23
        res = dir(ins)
        return f"применение метода dir() словаря:\nd = {ins}\nперечисляются атрибуты и методы словаря:\ndir = dir(d)\n{res}"

    def create_hand_set(self, ins):#24
        return f"создание множества добавлением элементов вручную. Элементами множества\n" \
               f"могут быть только неизменяемые типы элементов, поэтому словари и списки не могут быть\n" \
               f"элементам множества. Кроме того, все элементы множества уникальны, повторы исключены\n" \
               f"m = {ins}"

    def create_set_list(self, ins):#25
        l = [1, 2, False, 'val', (5, True, 'val1'), 1, 'val']
        m = set(l)
        return f"cоздание множества из списка:\nобратите внимание: повторяющиеся элементы в исходном списке\n" \
               f"в итоговом множестве будут в единственном числе\nm = set({l})\n{m})"

    def create_null_set(self, ins):#26
        m = {}
        type_m = type(m)
        set_m = set()
        type_set = type(set_m)
        return f"создание пустого множества:\nне рекомендуется создаваать пустое множество через литерал {{}}\n" \
               f"так как это прведет к созданию пустого словаря:\nm = {{}}\ntype(m) = {type_m}\n" \
               f"для создания пустого множества используется функция set():\nset_m = set()\ntype(set_m) = {type_set}"

    def create_circle_set(self, ins):#27
        print(f"итерация по элементам множества производится с помощью цикла:\n"
              f"ins = {ins}\nfor m in ins:\n    print(m)\nрезультат:")
        for m in ins:
            print(m)
        return ''

    def create_in_set(self, ins):#28
        el = input(f"введите проверяемый элемент множества:\nm = {ins}\n")
        res = el in ins
        print(res)
        ans = 'элемент присутствует во множестве' if res is True else 'элемент отсутствует во множестве'
        return ans

    def create_add_set(self, ins):#29
        inp = input(f"добавление элемента множества.\nm = {ins}\nВведите новый элемент множества:\n")
        ins.add(inp)
        return f"m.add({inp})\nm = {ins}\nесли вы укажете уже существующий элемент, то он добавлен не будет."

    def create_discard_set(self, ins):#30
        inp = input(f"Удаление элемента множества методом discard()\n"
                    f"Eсли удаляем отсутствующий элемент множества - это не вызовет ошибку\n"
                    f"m = {ins}\nвведите удаляемый элемент:\ninp = ")
        ins.discard(inp)
        return f"m.discard(inp)\n{ins}"


    def create_remove_set(self, ins):#31
        inp = input(f"Удаление элемента множества методом remove()\n"
                    f"в отличие от метода discard() удаление отсутствующего элемента множества - вызовет ошибку\n"
                    f"m = {ins}\nвведите удаляемый элемент:\ninp = ")
        ins.remove(inp)
        return f"m.remove(inp)\n{ins}"

    def create_pop_set(self, ins):#32
        print(f"удаление и возврат удаленного или оставшихся элементов множества.\n"
              f"обращаем внимание, что выбрать удаляемый элемент невозможно, выбор произвольный\nm = {ins}\n")
        res = ins.pop()
        return f"возврат удаляемого элемента:\nprint(m.pop())\n{res}\n" \
               f"возврат итогового множества после удаления элемента:\nprint(m)\n{ins}"

    def create_clear_set(self, ins):#33
        print(f"удаление всех элементов множества с помощью метода clear():\n" \
              f"m = {ins}\nm.clear()")
        ins.clear()
        return f"результат\n{ins}"

    def create_union_set(self, ins):#34
        m1 = {1, 2, 3, 4, 5}
        m2 = {'val1', 'val2', 'val3', 'val4', 'val5'}
        m3 = ins
        m_res = m1.union(m2, m3)
        return f"объединение множеств:\nm1 = {m1}\nm2 = {m2}\nm3 = {m3}\nm_res = m1.union(m2, m3)\n" \
               f"альтернативный способ:\nprint(m1 | m2 | m3)\nm_res = {m_res}"

    def create_intersection_set(self, ins):#35
        m1 = {1, 2, 3, 4, 5, 'val', 'val1', 'val2'}
        m2 = ins
        m_res = m1.intersection(m2)
        return f"пересечение множеств:\nm1 = {m1}\nm2 = {m2}\nm_res = m1.intersection(m2)\n" \
               f"альтернативный способ:\nprint(m1 & m2)\nm_res = {m_res}"

    def create_isdisjoint_set(self, ins):#36
        m1 = {1, 2, 3, 4, 5}
        m2 = {6, 7, 8, 9}
        m3 = ins
        m_tr = m2.isdisjoint(m3)
        m_fl = m1.isdisjoint(m3)
        return f"проверка являются ли два множества пересекающимися или нет:\n" \
               f"m1 = {m1}\nm2 = {m2}\nm3 = {m3}\nпересекающиеся:\nm_fl = m3.isdisjoint(m1)\n" \
               f"{m_fl}\nне пересекающиеся:\nm_tr = m3.isdisjoint(m2)\n{m_tr}"


    def create_diff_set(self, ins):#37
        m1 = {1, 2, 3, 4, 5, 'val', 'val1'}
        m2 = ins
        diff_m = m1.difference(m2)
        sdiff_m = m1.symmetric_difference(m2)
        return f"определение разницы между множествами:\nm1 = {m1}\nm2 = {m2}\nразница множеств:\n" \
               f"diff_m = m1.difference(m2)\nальтернативный вариант:\ndiff_m = m1 - m2\nprint(diff_m)\n{diff_m}\n" \
               f"симметричная разница множеств:\nsdiff_m = m1.symmetric_difference(m2)\nальтернативный вариант:\n" \
               f"diff_m = m1 ^ m2\nprint(sdiff_m)\n{sdiff_m}"



    def create_compare_set(self, ins):#38
        m1 = {1, 2, 3, 4, 5, 'val', 'val1'}
        m2 = ins
        sub_m = m1.issubset(m2)
        super_m = m1.issuperset(m2)
        return f"сравнение множеств:\nm1 = {m1}\nm2 = {m2}\nявляется ли множество m1 дочерним для множества m2?:\n" \
               f"sub_m = m1.issubset(m2)\nальтернативный вариант:\nsub_m = m1 <= m2\nprint(sub_m)\n{sub_m}\n" \
               f"является ли множество m1 родительским для множества m2?:\n" \
               f"super_m = m1.issuperset(m2)\nальтернативный вариант:\nsub_m = m1 >= m2\nprint(super_m)\n{super_m}\n"

    def create_copy_set(self, ins):#39
        ins_copy = ins.copy()
        return f"создание копии множества:\nm = {ins}\nm_copy = m.copy()\nprint(m_copy)\n{ins_copy}"

    def create_len_set(self, ins):#40
        l = len(ins)
        return f"метод возвращает длину множества:\nm = {ins}\nprint(len(m))\n{l}"

    def create_frozenset_set(self, ins):#41
        list = [1, 2, 3, 4, 5]
        mfl = frozenset(list)
        mfm = frozenset(ins)
        return f"создание замороженного множества (неизменяемый тип данных):\n" \
               f"m = {ins}\nmfm = frozenset(m)\nprint(mfm)\n{mfm}\n\nl = {list}\n" \
               f"mfl = frozenset(l)\nprint(mfl)\n{mfl}"

    def create_other_set(self, ins):
        m = {1, 2, 3, 4, 5, -6}
        print(f"использование иных функций множеств:\nm = {ins}\nenumerate():\nfor el in enumerate(m):\n"
              f"    print(el)\n")
        for el in enumerate(ins):
            print(el)
        f_all = all(ins)
        f_any = any(ins)
        f_max = max(m)
        f_min = min(m)
        f_sum = sum(m)
        f_sort = sorted(m)
        return f"\nфункция all():\nprint(all(m))\n{f_all}\n\nфункция any():\nprint(any(m))\n{f_any}\n\n" \
               f"функция max():\nprint(max(m))\n{f_max}\n\nфункция min():\nprint(min(m))\n{f_min}\n\n" \
               f"функция sum():\nprint(sum(m))\n{f_sum}\n\nфункция sorted():\nprint(sorted(m))\n{f_sort}"






