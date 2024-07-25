values_list = [3, 'val_list', True]
values_dict = {'a': 8, 'b': 'val_dict', 'c': False}
values_list_2 = [54.32, 'Строка' ]

def print_params(a = 1, b = 'строка', c = True):
    return f"{a} '{b}' {c}"


print(print_params(*values_list))
print(print_params(**values_dict))
print(print_params(*values_list_2, 42))