def code_or_decode(alph, line, turn, direct):
    if direct == 0:  # Шифрование
        result = ""
        for i in line:
            if i in alph:
                indx = alph.index(i)
                result += alph[(indx + turn) % len(alph)]
        return result
    elif direct == 1:  # Дешифрование
        result = ""
        for i in line:
            if i in alph:
                indx = alph.index(i)
                result += alph[(indx - turn) % len(alph)]
        return result

rus = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'  # Без `ё`
nums = '1234567890'
smbs = ':; !&-+=()*/.,'
alph = rus + rus.upper() + nums + smbs

# Функция для тестов (возвращает алфавит без перемешивания)
def rand_alph(alph):
    return alph  # Просто возвращаем исходный алфавит

if __name__ == "__main__":
    line = input("Введите текст: ")
    turn = 3
    direct = int(input("Введите 0 - зашифровать или 1 - дешифровать: "))
    print(code_or_decode(rand_alph(alph), line, turn, direct))