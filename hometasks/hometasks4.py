my_string = input('Ведите текст: ')
print(f"Строка в верхнем регистре: {my_string.upper()},"
      f"\nСтрока в нижнем регистре: {my_string.lower()},"
      f"\nУдаляем пробелы вначале и конце строки: {my_string.strip()},"
      f"\nУдаляем все пробелы: {my_string.replace(' ', '')},"
      f"\nПервый символ строки: {my_string[0]},"
      f"\nПоследний символ строки: {my_string[-1]}")
