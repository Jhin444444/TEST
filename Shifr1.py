import random


def code_or_decode(alph,line, turn):
    if direct == 0: # шифрование
            result = "" 
            for i in line:
                if i in alph: # проверка
                    indx = alph.index(i) # узнаём индекс
                    result += alph[indx + turn] # прибавляем шаг
            return result        
    if direct == 1: # дешифрование       
            result = ""
            for i in line:
                if i in alph: # проверка
                    indx = alph.index(i) # узнаем индекс
                    result += alph[indx - turn] # вычитаем шаг  
            return result      


rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
nums = '1234567890'
smbs = ':; !&-+=()*/.,'
alph = rus + rus.upper() + nums + smbs  # алфавит

def rand_alph(alph): # перемешивание алфавита
    symbols = list(alph)
    random.shuffle(symbols) # случайное перемешивание символов
    return symbols

line = input("Введите текс: ") 

turn = 3  # шаг смещения по Цезарю

direct = int(input("Введите 0 - зашифровать или 1 - дешифровать: "))
print(code_or_decode(rand_alph(alph), line, turn))

