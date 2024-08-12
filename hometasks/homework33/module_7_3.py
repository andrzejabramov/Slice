import os
import string


class WordsFinder:
    def __init__(self, *file_name):
         self.file_name = file_name

    def __create_directory(self):
        dir = input('Введите название директории: ')
        try:
            os.mkdir(r'./'+dir)
        except FileExistsError:
            print(f"Директория с именем {dir} уже существует, действия будут производиться в существующей директории")
        return dir

    def __yes_no(self):
        ch = input('Для добавления изменений в существующий файл нажмите аббревиатуру Save - символ S\n'
                   'чтобы оставить только новые данные нажмите символ R\n'
                   'чтобы сохраниить новый файл с другим именем, нажмите аббревиатуру Save As - символы SA\n'
                   'чтобы закрыть файл без сохранения, нажмите аббревиатуру Cancel - символ C\n')
        while True:
            if ch.upper() == 'S' or ch.upper() == 'R' or ch.upper() == 'SA' or ch.upper() == 'C':
                return ch.upper()
            ch = input('Введен неверный символ, повторите ввод: ')

    def __add_text(self, name_file):
        txt = input(f"Введите текст через запятую, например text1, text2, text3 для файла {name_file}: ")
        return txt.replace(', ', ''+'\n')

    def create_file(self):
        d = self.__create_directory(); file_list = self.file_name; attr = None
        for fl in file_list:
            try:
                with open(r'./'+d+'/'+fl, 'x', encoding='utf-8') as fn:
                    fn.write(self.__add_text(fl))
            except FileExistsError:
                print(f"Файл с именем {fl} уже есть в директории")
                ch = self.__yes_no()
                if ch == 'C':
                    print(f"Файл {fl} остался без изменений")
                else:
                    if ch == 'S':
                        attr = 'a'
                    elif ch == 'R':
                        attr = 'w'
                    elif ch == 'SA':
                        fl = input('Введите название нового файла: ')
                        attr = 'x'
                    with open(r'./' + d + '/'+ fl, attr, encoding='utf-8') as file:
                        file.write('\n'+self.__add_text(fl)) if ch == 'S' else file.write(self.__add_text(fl))
        return ''

    def get_all_words(self):
        all_words = {}; punkt = [',', '.', '=', '!', '?', ';', ':', ' - ']
        dir = self.__create_directory(); file_list = self.file_name
        for fl in file_list:
            with open(r'./'+dir+'/'+fl, 'r') as fn:
                txt = fn.read()
            for symb in punkt:
                if symb in txt:
                    #txt.translate(str.maketrans('', '', string.punctuation))
                    txt = txt.replace(symb, ' ')
                    txt = txt.replace('\n', ' ')
            txt = txt.lower().split()
            txt = list(txt)
            all_words[fl] = txt
        return all_words

    def find(self, word):
        d = {}; l = list(self.get_all_words().items())
        for tup in l:
            if word in tup[1]:
                d[tup[0]] = tup[1]
        return d

    def count(self, word):
        d = {}; l = list(self.get_all_words().items())
        for tup in l:
            count = 0
            for w in tup[1]:
                if w.find(word) != -1:
                    count += 1
            d[tup[0]] = count
        return d


wf = WordsFinder('text1.txt', 'text2.txt', 'text3.txt')
# print(wf.get_all_words())
# print(wf.find('это'))
# print(wf.count('а'))
print(wf.create_file())
