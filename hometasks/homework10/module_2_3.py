my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
count = 0


while my_list[count] >= 0:
    print(my_list[count])
    count += 1
    if count < len(my_list):
        continue
    else:
        break