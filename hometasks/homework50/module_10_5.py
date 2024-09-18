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
    return f'записей во всех файлах: {len(all_data)}'


filenames = [f'./Files/file {number}.txt' for number in range(1, 5)]
time_start = datetime.now()
##линейный вызов
#print(read_info(filenames))
##многопроцессорный
if __name__=='__main__':
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
time_end = datetime.now()
time_res = time_end - time_start
print(time_res)

