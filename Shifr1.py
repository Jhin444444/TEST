import random


def code_or_decode(alph,line, turn):
    if direct == 0: # шифрование
            res = "" 
            for i in line:
                if i in alph: # проверка
                    indx = alph.index(i) # узнаём индекс
                    res += alph[indx + turn] # прибавляем шаг
            return res        
    if direct == 1: # дешифрование       
            res = ""
            for i in line:
                if i in alph: # проверка
                    indx = alph.index(i) # узнаем индекс
                    res += alph[indx - turn] # вычитаем шаг  
            return res      


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

