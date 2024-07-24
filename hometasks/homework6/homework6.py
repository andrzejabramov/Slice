from classes import Dict_list

ch = {}
n = ''
descript = ''
cl = Dict_list(ch, n, descript)

print('работа со словарем')
d = {'name': 'Andrey', 'age': 61, 'location': 'Krasnodar'}
print(f"вывод словаря: {d}")

key = input('введите ключ: ')
try:
    valid_key = d[key]
    print(f"вывод существующего ключа: {valid_key}")
except Exception:
    invalid_key = d.get(key)
    print(f"вывод несуществующего ключа без ошибки: {invalid_key}")

d.update({'school': 'Urban', 'date_birth': '12.11.1962'})
print(f"добавляем два элемента:\nd.update({{'school': 'Urban', 'date_birth': '12.11.1962'}})\nрезультат:\n{d}")
d_del = d.pop('date_birth')
print(f"удаляем элемент по ключу date_birth, выводим в консоль значение удаленного элемента:\n"
      f"d_del = d.pop('date_birth')\nрезультат:\n{d_del}")
print(f"выводим в консоль результирующий словарь:\n{d}")

print('\nработа с множествами')
my_set = {1, 1, 'val', 'val', 4.0, (True, 2, 'val1')}
print(f"создаем множество:\nmy_set = {my_set}")
my_set.update('5z')
print(f"добавляем два элементв множества вариант1:\nmy_set.update('5z')\n{my_set}")
my_set.update([6, 'y'])
print(f"вариант2 через список:\nmy_set.update([6, 'y'])\n{my_set}")
my_set.update((7, 'val8'))
print(f"вариант3 через кортеж:\nmy_set.update((7, 'val8'))\n{my_set}")
res = my_set.pop()
print(f"удаление и возвращение на печать в консоль удаленного элемента:\nres = my_set.pop()\n"
      f"указать конкретный элемент множества невозможно, будет удален произвольный элемент"
      f"\n{res}\nвывод в консоль результирующего множества:\n{my_set}\n")

set_discard = cl.create_discard_set(my_set)
print(f"чтобы на данном этапе не усложнять код с учетом формата удаляемых элементов\n"
      f"пожалуйста вводите для удаления строковые элементы (в одинарных кавычках)\n{set_discard}")

set_remove = cl.create_remove_set(my_set)
print(f"обращаем внимание: при выборе для удаления элементов числового формата,\n"
      f"результат выдаст ошибку!\n{set_remove}")