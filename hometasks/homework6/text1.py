import re

# regex = r"\d|None"
# b = input()
# с = b if re.findall(regex, b) else None
# print(с)

# pattern = re.compile(ur'None')
# str = u''
# print(pattern.search(str))

# d = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3', 'key4': 'val4', 'key5': 'val5', 'key6': 'val6'}
# # print(type(d))
# print(len(dict({\'key1\': \'val1\', \'key2\': \'val2\', \'key3\': \'val3\', \'key4\': \'val4\', \'key5\': \'val5\', \'key6\': \'val6\'}')))


d = '{\'key1\': \'val1\', \'key2\': \'val2\'}'
a = input()
while True:
    try:
        a = eval(a)
        print(a)
        break
    except Exception:
        print('err')
        a = input()



