mutable_list = [1, 'abc', False]
immutable_var = ('abc', 1, True, mutable_list)
print(f"Выведем в консоль кортеж: {immutable_var},\n"
      f"Кортеж являетя обектом неизменяемым, за исключением, если\n"
      f"элементом кортежа является список, который можно изменять.\n"
      f"Выведем изменненный список в кортеже:")
mutable_list[-1] = True
print(immutable_var)