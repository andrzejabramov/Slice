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

class Dict_list:
    def input_data(self):
        ins = input(descript)
        match ins:
            case '1':
                return self.create_literal()
            case '2':
                return self.create_fdict()
            case '3':
                return self.create_fromkeys()
            case '4':
                return self.create_zip()
            case '5':
                return self.create_comprehension()
            case '6':
                return self.create_copy()
            case '7':
                return self.create_getdata()
            case '8':
                return self.create_get_dict(note='Введите несуществующий ключ для проверки метода get() d = {\'key1\': \'val1\', \'key2\': 2, \'key3\': True}: ')
            case '9':
                return self.create_key_dict()
            case '10':
                return self.create_val_dict()
            case '11':
                return self.create_items_dict()
            case '12':
                return self.create_iter_dict()

    def create_literal(self):
        d = {'key1': 1, 'key2': 'val2', 'key3': True}
        return 'литерала\nd = {}\nd = ' + f"{d}"


    def create_fdict(self):
        d = dict(key1='val1', key2=2, key3=False)
        return f"функции dict\nd = dict(key1=\'val1\', key2=2, key3=False)\nprint(d)\n{d}"

    def create_fromkeys(self):
        d = dict.fromkeys(['key1', 'key2'], 'val')
        return f"метода fromkeys\nd = dict.fromkeys([\'key1\', \'key2\'], \'val\')\nprint(d)\n{d}"

    def create_zip(self):
        key_list = ['key1', 'key2', 'key3']
        val_list = ['val', 1, True]
        result_dict = dict(zip(key_list, val_list))
        return f"архива zip\nkey_list = [\'key1\', \'key2\', \'key3\']\n" \
        f"val_list = [\'val\', 1, True]\n" \
        f"result_dict = dict(zip(key_list, val_list))\n" \
        f"print(result_dict)\n{result_dict}"

    def create_comprehension(self):
        d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        d1 = {k: v * 2 for (k, v) in d.items()}
        return f"генераторов словарей\nd = {d}\n" + 'd1 = {k: v * 2 for (k, v) in d.items()}\n' + f"print(d1)\n{d1}"

    def create_copy(self):
        d = {'key1': 'val1', 'key2': 2, 'key3': True}
        id_d = id(d)
        d_copy = d.copy()
        id_d_copy = id(d_copy)
        return f"Исходный словарь: d = {d}\n" \
               f"Eго id в памяти:\nid_d = id(d)\n{id_d}\nНовый экземпляр словаря, скопированный из исходного:\n" \
               f"d_copy = d.copy()\n{d_copy}.\n" \
               f"Его id в памяти:\nid_d_copy = id(d_copy)\n{id_d_copy}\nотличается от исходного"

    def create_getdata(self, note='указанный ключ отсутствует в словаре. Для устранения ошибки используйте метод get()'):
        d = {'key1': 'val1', 'key2': 2, 'key3': True}
        key = input(f"Введите ключ для получения значения из словаря d = {d}: ")
        try:
            res = d[key]
            return res
        except:
            return note

    def create_get_dict(self, note):
        d = {'key1': 'val1', 'key2': 2, 'key3': True}
        key = input(note)
        res = d.get(key)
        if res is None:
            return res
        else:
            note = 'Вы ввели существующий ключ, введите пожалуйста не существующий: '
            return self.create_get_dict(note)

    def create_key_dict(self):
        d = {'key1': 'val1', 'key2': 2, 'key3': True}
        res = d.keys()
        return f"получаем список ключей словаря:\nd = {d}\nres = d.keys()\nres = {res}"

    def create_val_dict(self):
        d = {'key1': 'val1', 'key2': 2, 'key3': True}
        res = d.values()
        return f"получаем список значений словаря:\nd = {d}\nres = d.values()\nres = {res}"

    def create_items_dict(self):
        d = {'key1': 'val1', 'key2': 2, 'key3': True}
        res = d.items()
        return f"получаем список кортежей ключ-значение словаря:\nd = {d}\nres = d.items()\nres = {res}"

    def create_iter_dict(self):
        d = {'key1': 'val1', 'key2': 2, 'key3': True}
        print(f"итерируем словарь по ключам:\n{d}\nfor key in d:\n    print(key)")
        for key in d:
            print(key)
        print(f"итерируем словарь по парам ключ-значение:\n{d}\nfor key, value in d.items():\n    print(key, value)")
        for key, value in d.items():
            print(key, value)
        return ''


