from classes import Dict_list


d = {-1: 'val1', 'key2': 2, 'key3': True, 'key4': [('o', 1), ('p', 2), ('q', 3)], 'key5': {'key': 'val'}, 'key6': None}
m = {1, 'val', True}
ch = {}
n = ''
descript = ''

cl = Dict_list(ch, n, descript)

def choice ():
    list_method = cl.descr()
    num_method = input(list_method)
    answer = cl.valid_metod(num_method, list_method)
    ch = d if answer is True else m
    return cl.input_data(num_method, ch)


if __name__ == '__main__':
    print(choice())