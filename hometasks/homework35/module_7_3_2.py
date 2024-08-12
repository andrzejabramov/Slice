import os
import time


root = '../homework33'

for root, dirs, files in os.walk(root):
    for name in files:
        path = os.path.join(root, name)
        create_file = time.strftime("%d.%m.%Y %H:%M", time.localtime(os.path.getctime(path)))
        modify_file = time.strftime("%d.%m.%Y %H:%M", time.localtime(os.path.getmtime(path)))
        size = os.path.getsize(path)
        drct = os.path.dirname(path)
        print(f"Файл {name} в директории {drct} имеет размер {size} байт " \
              f"был создан {create_file} и модифицирован {modify_file}")
