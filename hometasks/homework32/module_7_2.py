info = [
   'Text for tell.',
   'Используйте кодировку utf-8.',
   'Because there are 2 languages!',
   'Спасибо!'
   ]


def custom_write(file_name, string):
    num_str = 1
    d = {}
    file = open(file_name, 'a', encoding='utf-8')
    for el in string:
        byte = file.tell()
        """
        При записи текста в файл исключаем \n у последнего элемента списка текста (пееменной info), 
        Для того, чтобы байты начала новых строк сошлись с указанным в задании пришлось добавить
        пробел перед \n
        """
        file.write(el) if el == string[-1] else file.write(el+' \n')
        d[(num_str, byte)] = el
        num_str += 1
    file.close()
    return d

result = custom_write('write.txt', info)
for elem in result.items():
    print(elem)