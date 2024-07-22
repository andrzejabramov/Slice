grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
new_grades = []
for el in grades:
    med = sum(el) / len(el)
    new_grades.append(med)
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_sort = sorted(students)
res_dict = dict(zip(students_sort, new_grades))
print(res_dict)