def ancient_cipher():
    note = 'Введенные данные не удовлетворяют условию! Повторите ввод:'
    result = ''
    while True:
        d = input('Введите случайное целое число в диапазоне от 3 до 20: ')
        try:
            d = int(d)
            if d > 2 and d < 21:
                for step in range(1, d):
                    for substep in range(step+1, d):
                        if d % (step + substep) == 0:
                            result = result + str(step)+str(substep)
                break
            else:
                print(note)
        except Exception:
            print(note)
    return result


print(ancient_cipher())