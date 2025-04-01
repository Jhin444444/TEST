import random


def code_or_decode(alph, line, turn, direct):  # Добавлен параметр direct
    if direct == 0:  # Шифрование
        result = ""
        for i in line:
            if i in alph:
                indx = alph.index(i)
                result += alph[(indx + turn) % len(alph)]  # Защита от выхода за границы
        return result
    elif direct == 1:  # Дешифрование
        result = ""
        for i in line:
            if i in alph:
                indx = alph.index(i)
                result += alph[(indx - turn) % len(alph)]
        return result    


rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
nums = '1234567890'
smbs = ':; !&-+=()*/.,'
alph = rus + rus.upper() + nums + smbs  # алфавит

def rand_alph(alph): # перемешивание алфавита
    symbols = list(alph)
    # random.shuffle(symbols) # случайное перемешивание символов
    return symbols

line = input("Введите текст: ") 

turn = 3  # шаг смещения по Цезарю

direct = int(input("Введите 0 - зашифровать или 1 - дешифровать: "))
print(code_or_decode(rand_alph(alph), line, turn))

