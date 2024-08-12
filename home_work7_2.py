info = ['Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!']
def custom_write(file_name, strings):
    strings_positions = {}
    for x in strings:
        file = open(file_name, 'a', encoding='utf-8')
        key_1 = strings.index(x) + 1
        key_2 = file.tell()
        strings_positions[key_1, key_2] = x
        file.write(f'{x}\n')
        file.close()
    return strings_positions

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
