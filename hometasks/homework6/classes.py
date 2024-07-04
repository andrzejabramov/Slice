descript = 'Выберите цифру для просмотра варианта создания словаря с помощью:\n'
'1 литерала\n'
'2 функции dict\n'
'3 метода fromkeys (значения ключей по умолчанию)\n'
'4 архива zip\n' \
'5 генераторов словарей\n'

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

    def create_literal(self):
        return 'литерала\nd = {}\nd = {\'key1\': 1, \'key2\': True}'

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
        return 'генераторов словарей\nd = {\'a\': 1, \'b\': 2, \'c\': 3, \'d\': 4, \'e\': 5}\n' \
        'd1 = {k: v * 2 for (k, v) in d.items()}\n' \
        f"print(d1)\n{d1}"
