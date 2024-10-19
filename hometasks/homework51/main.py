from classes import WordsFinder
import inspect
import re


a = 'sf'
b = True
f = 45.7896
d = {'key1': 'val1', 'key2': 'val2'}
dig = 56
l = [1, 'fgh', True, [1, 2, 3]]
m = {'tyu', 2, False}
k = ('a', 'b', 'c')

def test_func(a, b, c):
    return str(a + b) + c


wf = WordsFinder('test.py')


def introspection_info(obj):
    d = {}
    a = []
    m = []
    type_val = str(type(obj))[8:len(str(type(obj))) - 2]
    module_name = inspect.getmodule(obj)
    if module_name != None:
        module_name = str(module_name)[9:]
        module_name = module_name[:re.search(r'\s', module_name).start() - 1]
    for attr in dir(obj):
        if callable(getattr(obj, attr)):
            m.append(attr)
        else:
            a.append(attr)
    d.update({
        'type': type_val,
        'attributes': a,
        'methods': m,
        'module': module_name
    })
    return d


print(introspection_info(wf))





