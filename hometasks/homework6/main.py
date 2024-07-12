from classes import Dict_list


d = {1: 'val1', 'key2': 2, 'key3': True, 'key4': [('o', 1), ('p', 2), ('q', 3)], 'key5': {'key': 'val'}, 'key6': None}

cl = Dict_list(d)


#print(cl.input_data(d))


if __name__ == '__main__':
    print(cl.input_data(d))