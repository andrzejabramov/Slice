first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']


first_result = [len(el) for el in first_strings if len(el) >= 5]
second_result = [(el, elm) for el in first_strings for elm in second_strings if len(el) == len(elm)]
third_result = {el: len(el) for el in first_strings + second_strings if len(el) % 2 == 0}


print(first_result)
print(second_result)
print(third_result)
