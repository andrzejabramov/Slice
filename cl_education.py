#создаем класс для вывода различных значений slice строки
class ClicesSolution:
    def input_text(self, descript_err):
        #метод ввода и валидации значений. Для перестраховки input() обернут в класс str()
        act = str(input('введите любой набор символов более одного: '))
        if len(act) == 1: #обработка ошибки валидации ввода
            print(descript_err)
            return self.input_text(descript_err)
        return act

    def first_index(self, descript_err): #метод вывода первого символа строки
        act_f = self.input_text(descript_err)
        return act_f[0]

    def last_index(self, descript_err): #метод вывода последнего символа строки
        act_l = self.input_text(descript_err)
        return act_l[-1]

    def str_reverse(self, descript_err): #метод вывода строки наоборот
        act_r = self.input_text(descript_err)
        return act_r[::-1]

    def str_through(self, descript_err): #метод вывода каждого второго символа строки
        act_t = self.input_text(descript_err)
        return act_t[1::2]

    def reverse_half(self, descript_err):
        #метод вывода второй половины строки в обратном порядке при условии, что эта половина всегда больше остатка
        act_h = self.input_text(descript_err)
        len_str = len(act_h)
        if (len_str // 2) % 2 == 0:
            n = len_str - len_str//2 - 2
        else:
            n = len_str - len_str//2 - 1 if len_str % 2 == 0 or len_str == 3 else len_str - len_str // 2 - 3
        return act_h[:n:-1]


