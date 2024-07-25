data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
count = 0

def calculate_structure_sum(data_structure):
    global count
    for element in data_structure:
        if isinstance(element, int) or isinstance(element, float):
            count = count + element
        elif isinstance(element, str):
            count = count + len(element)
        elif isinstance(element, dict):
            l_dict = list(element.keys()) + list(element.values())
            calculate_structure_sum(l_dict)
        elif isinstance(element, list) or isinstance(element, tuple) or isinstance(element, set):
            calculate_structure_sum(element)
    return count


result = calculate_structure_sum(data_structure)
print(f"result = {result}")