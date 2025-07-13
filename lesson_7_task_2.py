# Дана строка, длина которой не превосходит 1000. Вам требуется преобразовать все идущие подряд пробелы в один. Выведите измененную строку.
original_line = input()

while '  ' in original_line:
    original_line = original_line.replace('  ', ' ')

print(original_line)