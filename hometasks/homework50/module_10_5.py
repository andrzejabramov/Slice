import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    for n in name:
        count = 0
        with open(n, 'r', encoding='utf-8') as f:
            while True:
                content = f.readline()
                if not content:
                    break
                all_data.append(content)
                count += 1
            print(f'строк в файле {n}: {count}')
    return len(all_data)


start = datetime.now()

###линейный вызов
# filenames = [f'./Files/file {number}.txt' for number in range(1, 5)]
# print(f'строк во всех файлах: {read_info(filenames)}')

###многопроцессорный
#if __name__ == '__main__':
    # filenames = [[f'./Files/file {number}.txt'] for number in range(1, 5)]
    # with multiprocessing.Pool(processes=4) as pool:
    #     print(f'строк во всех файлах: {sum(pool.map(read_info, filenames))}')
    #     pool.close()
    #     pool.join()

print(f'Время выполнения задачи: {datetime.now() - start}')

