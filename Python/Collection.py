from random import *
import random
from math import *
import time

def collection():
    while True:
        lst = ["caesarCiper", "tournament", "randomGeometric", "kknb", "quadroFunction", "numericGuesser", "quarter", "time", "yep"]
        programms = len(lst)
        width = 48
        print(f"╔", "═"*width, "╗\n", "║", " "*((width-2)//2), "COLLECTION", " "*((width-2)//2), "║", sep="")
        print("╠", "═"*3, "╦", "═"*(width-4), "╣", "\n", "║ 1", " ║ ", lst[0], " "*(width-11), "║", sep="")
        for num in range(1, programms):
            print("╠", "═"*3, "╬", "═"*(width-4), "╣", "\n", "║ ", num+1, " ║ ", lst[num], " "*(width-12), "║", sep="")
        print("╚", "═"*3, "╩", "═"*(width-4), "╝", sep="")
        choice = int(input("\n• Choice mini-programm -> "))
    
        #   ╔ ╗ ║ ╚ ╝ ═ ╠ ╣ ╦ ╩ ╬
        if choice == 1:
            mainCaesarCiper()
        elif choice == 2:
            tournament()
        elif choice == 3:
            randomGeometric()
        elif choice == 4:
            kknb()
        elif choice == 5:
            quadroFunction()
        elif choice == 6:
            numericGuesser()
        elif choice == 7:
            quarter()
        elif choice == 8:
            time()
        elif choice == 9:
            yep()
        elif choice > len(lst):
            print("\nНет такой мини-программы!")
            

# CAESARCIPER


def caesarCipher(lang, text, shift, decrypt=False):
    ru_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    en_alphabet = 'abcdefghijklmopqrsotuvwxyz'
    alphabet = ''
    result = ''
    if lang == 1:
        alphabet = ru_alphabet
    elif lang == 2:
        alphabet = en_alphabet
    if decrypt:
        shift = -shift
    for char in text:
        if char.lower() in alphabet:
            pos = alphabet.find(char.lower())
            # Вычисляем новую позицию с учётом сдвига и «закольцовывания»
            new_pos = (pos + shift) % len(alphabet)
            if char.isupper():
                result+= alphabet[new_pos].upper()
            else:
                result += alphabet[new_pos]
        else:
            result += char
    return result

def mainCaesarCiper():
    while True:
        lang = int(input("""
    +-----Шифр-Цезаря-----+
    | 1. Русский язык     |
    | 2. Английский язык  |
    | 3. Выход            |
    +---------------------+
    • Выберите язык (1-2): """))
        while True:
            if lang > 2:
                print("\n\n    Неверный выбор! Попробуйте снова.")
                break
            elif lang == 1:
                choice = int(input("""
    +-Шифр-Цезаря-(Русский алфавит)-+
    | 1. Зашифровать                |
    | 2. Расшифровать               |
    | 3. Выход                      |
    +-------------------------------+
    • Выберите действие (1-3): """))
                if choice == 3:
                    break
                elif choice > 3:
                    print("\n\n    Неверный выбор! Попробуйте снова.")
                elif choice in (1, 2):
                    text = input("\n    • Введите текст: ")
                    shift = int(input("    • Введите сдвиг (целое число): "))
                    if choice == 1:
                        result = caesarCipher(lang, text, shift)
                        print("\n    Зашифрованный текст:", result, shift)
                    else:
                        result = caesarCipher(lang, text, shift, decrypt=True)
                        print("\n    Расшифрованный текст:", result)
            elif lang == 2:
                choice = int(input("""
    +-Caesar-Ciper-(English alphabet)--+
    | 1. Encrypt                       |
    | 2. Decrypt                       |
    | 3. Quit                          |
    +----------------------------------+
    • Choose action (1-3): """))
                if choice == 3:
                    break
                elif choice > 3:
                    print("\n\n    Incorrect choice! Please try again.")
                elif choice in (1, 2):
                    text = input("\n    • Enter text: ")
                    shift = int(input("    • Enter shift (Integer): "))
                    if choice == 1:
                        result = caesarCipher(lang, text, shift)
                        print("\n    Encrypted text:", result, shift)
                    else:
                        result = caesarCipher(lang, text, shift, decrypt=True)
                        print("\n    Decrypted text:", result)


# TOURNAMENT


def tournament():
    while True:
        choice1 = int(input("""
    +---Турнир------------------+
    | 1. Ввести несколько чисел |
    | 2. Выход                  |
    +---------------------------+
    -> """))
        if choice1 == 2:
            break
        elif (choice1 < 1) or (choice1 > 2):
            print("""
    +---Бот----------------------------------------------+
    | Данный символ из таблицы ASCII                     |
    | не подходит для выбора действия в данной программе |
    +----------------------------------------------------+""")
        elif choice1 == 1:
            round_num = 1
            numbers = list(map(int, input("""
    +---Бот------------------------------+
    | Пожалуйста введите несколько чисел |
    | через пробел ниже                  |
    +------------------------------------+
    -> """).split()))
            nums_dict = {num: random.choice(["yes", "no"]) for num in numbers}
                    
            while len(nums_dict) > 1:
                print(f"""
    +---Бот----------------+
    | Ваш набор на раунд {round_num} |
    +----------------------+""")
                max_len = max(len(str(num)) for num in nums_dict)
                for i, (num, value) in enumerate(nums_dict.items(), start=1):
                    print(f"\n{" "*4}{i}. {num:>{max_len}}: {value}", end="")
                choice2 = int(input(f"""\n
    +---Бот--------------+
    | Готовы к раунду {round_num+1}? |
    +--------------------+
    | 1. Да              |
    +--------------------+
    -> """))
                nums_dict = {num: random.choice(["yes", "no"]) for num, value in nums_dict.items() if value == "yes"}
                round_num += 1
                
            if len(nums_dict) == 1:
                winner = next(iter(nums_dict))
                choice3 = int(input(f"""
    +---Бот----------------------------------+
    | У нас есть победитель, число {winner}!        |
    +----------------------------------------+
    | 1. Перезапуск                          |
    | 2. Выход                               |
    +----------------------------------------+
    -> """))
                if choice3 == 2:
                    break
            else:
                choice3 = int(input(f"""
    +---Бот-------------------------+
    | Ни одно из чисел не победило! |
    +-------------------------------+
    | 1. Перезапуск                 |
    | 2. Выход                      |
    +-------------------------------+
    -> """))
                if choice3 == 2:
                    break
    
    
# RANDOMGEOMETRIC


def randomGeometric():
    S = randint(1, 101)
    P = randint(1, 41)
    print(f"""
    +---Бот--------------------------------+
    | Совпадут ли условные площадь ({S}) и |
    | периметр ({P}) с рандомными?         |
    | Сколько тестов необходимо?           |
    +--------------------------------------+
    | 1. 15 тестов                         |
    | 2. 30 тестов                         |
    | 3. 100 тестов                        |
    | 4. Ввести своё кол-во тестов         |
    | 5. Выход                             |
    +--------------------------------------+""")
    
    def do(num):
        for i in range(num):
            a = randint(1,10)
            b = randint(1,10)
            print(f"      {i+1}. randS ({a*b}), randP ({2*(a+b)})")
            if (a*b) == S:
                print(f"        !!! randS (a={a}, b={b}) !!!")
                break
            elif (2*(a+b)) == P:
                print(f"        !!! randP (a={a}, b={b}) !!!")
                break
            elif ((a*b) == S) and ((2*(a+b)) == P):
                print(f"        !!! randS, randP (a={a}, b={b}) !!!")
                break
                
    while True:
        choice = int(input("""    • Выберите действие -> """))
        if choice == 1:
            do(15)
        elif choice == 2:
            do(30)
        elif choice == 3:
            do(100)
        elif choice == 4:
            choice2 = int(input("""
    • Введите ваше число -> """))
            do(choice2)
        elif choice == 5:
            print("""
    +---Бот-------+
    | Досвидания! |
    +-------------+""")
            break
        elif choice > 5:
            print("""
    +---Бот--------------+
    | Некоректный выбор! |
    +--------------------+""")


# KKNB


def kknb():
    sp = ["Камень", "Ножницы", "Бумага", "Колодец"]
    round_num = 1
    flag = True
    while flag == True:
        rsp = sp[randint(0,3)]
        
        print(f"""
    +---Бот---------------------+
    | Что вы выберите? Раунд: {round_num} |
    +---------------------------+
    | к: {sp[0]},                |
    | н: {sp[1]},               |
    | б: {sp[2]},                |
    | кол: {sp[3]}              |
    | или с вас 5х: 5хватит?      |
    +---------------------------+""")
        my = input("""    
    • Ваш выбор-> """)
        round_num += 1
        if (my == "5хватит") or (my == "5х"):
            print("""
    +---Бот---+
    | Хорошо. |
    +---------+""")
            flag = False
                
        elif (my == "Камень") or (my == "к") or (my == "Ножницы") or (my == "н") or (my == "Бумага") or (my == "б") or (my == "Колодец") or (my == "кол"):
            print(f"""
    +---Бот---------------------+
    | У меня {rsp}            |""")
        
            if (my == "Камень") or (my == "к") and (rsp == "Камень"):
                print("""    | У вас - Камень            |
    | (#) Ничья. (#)            |
    +---------------------------+""")
            elif (my == "Камень") or (my == "к") and (rsp == "Ножницы"):
                print("""    | У вас - Камень            |
    | (^^) Вы победили! (^^)    |
    +---------------------------+""")
            elif ((my == "Камень") or (my == "к")) and (rsp == "Бумага"):
                print("""    | У вас - Камень            |
    | (*v*) Я победил! (*v*)    |
    +---------------------------+""")
            elif ((my == "Камень") or (my == "к")) and (rsp == "Колодец"):
                print("""    | У вас - Камень            |
    | (*v*) Я победил (*v*)     |
    +---------------------------+""")
            
            elif ((my == "Ножницы") or (my == "н")) and (rsp == "Камень"):
                print("""    | У вас - Ножницы           |
    | (*v*) Я победил! (*v*)    |
    +---------------------------+""")
            elif ((my == "Ножницы") or (my == "н")) and (rsp == "Ножницы"):
                print("""    | У вас - Ножницы           |
    | (#) Ничья. (#)            |
    +---------------------------+""")
            elif ((my == "Ножницы") or (my == "н")) and (rsp == "Бумага"):
                print("""    | У вас - Ножницы           |
    | (^^) Вы победили! (^^)    |
    +---------------------------+""")
            elif ((my == "Ножницы") or (my == "н")) and (rsp == "Колодец"):
                print("""    | У вас - Ножницы           |
    | (*v*) Я победил! (*v*)    |
    +---------------------------+""")
            
            elif ((my == "Бумага") or (my == "б")) and (rsp == "Камень"):
                print("""    | У вас - Бумага            |
    | (^^) Вы победили! (^^)    |
    +---------------------------+""")
            elif ((my == "Бумага") or (my == "б")) and (rsp == "Ножницы"):
                print("""    | У вас - Бумага            |
    | (*v*) Я победил! (*v*)    |
    +---------------------------+""")
            elif ((my == "Бумага") or (my == "б")) and (rsp == "Бумага"):
                print("""    | У вас - Бумага            |
    | (#) Ничья. (#)            |
    +---------------------------+""")
            elif ((my == "Бумага") or (my == "б")) and (rsp == "Колодец"):
                print("""    | У вас - Бумага            |
    | (^^) Вы победили! (^^)    |
    +---------------------------+""")
            
            elif ((my == "Колодец") or (my == "кол")) and (rsp == "Камень"):
                print("""    | У вас - Колодец           |
    | (^^) Вы победили! (^^)    |
    +---------------------------+""")
            elif ((my == "Колодец") or (my == "кол")) and (rsp == "Ножницы"):
                print("""    | У вас - Колодец           |
    | (^^ Вы победили! (^^)     |
    +---------------------------+""")
            elif ((my == "Колодец") or (my == "кол")) and (rsp == "Бумага"):
                print("""    | У вас - Колодец           |
    | (*v*) Я победил! (*v*)    |
    +---------------------------+""")
            elif ((my == "Колодец") or (my == "кол")) and (rsp == "Колодец"):
                print("""    | У вас - Колодец           |
    | (#) Ничья (#)             |
    +---------------------------+""")
        else:
            print("""
    +---Бот---------------------+
    | Что это? Давайте ещё раз. |
    +---------------------------+""")
            
  
# NUMERICGUESSER


def numericGuesser():
    choice = int(input("""
    +---Числовая-Угадайка---+
    | 1. Бот (Программа)    |     
    | 2. Игрок (Вы)         |
    | 3. Выход              |
    +-----------------------+
    • Кто будет угадывать? -> """))

    if choice == 3:
        print("""
    +---Бот-------+
    | Досвидания! |
    +-------------+""")
        return
        
    elif choice > 3:
        print("""
    Введённый номер некоректен!""")
    
    elif choice == 1:
        a1, a2, count = 1, 80, 1
        my_n = int(input(f"""
    +---Бот-----------------+
    | Я угадываю. Загадайте |
    | число от {a1} до {a2}      | 
    +-----------------------+
    -> """))
        if (my_n < a1) or (my_n > a2):
            print("""
    Ваше число не входит в диапозон!""")
            return
        while True:
            a = randint(a1, a2)
            otva = input(f"""
    +---Бот--------------------------+
    | Я думаю это число  {a} {a1, a2}. |
    | Укажите насколько ваше         |
    | число отличается от моего      |
    | 1. Больше                      |
    | 2. Меньше                      |
    | 3. Равно                       |
    +--------------------------------+
    • -> """).lower()
            if otva == 1:
                a1 = a+1
                count += 1
            elif otva == 2:
                a2 = a-1
                count += 1
            elif otva == 3 and my_n == a:
                print("""
    +---Бот---------------------------+
    | Ура! Я угадал ваше число!       |""")
                if (count == 1):
                    print("""
    | С первого раза!!!               |
    +---------------------------------+""")
                elif (count == 2) or (count == 3) or (count == 4) or (count % 10 == 2) or (count % 10 == 3) or (count % 10 == 4):
                    print(f"""
    | Всего лишь за {count} попытки!  |
    +---------------------------------+""")
                elif (count == 5) or (count == 6) or (count == 7) or (count == 8) or (count == 9) or (count % 10 == 5) or (count % 10 == 6) or (count % 10 == 7) or (count % 10 == 8) or (count % 10 == 9) or (count % 10 == 0): 
                    print(f"""
    | За {count} попыток!             |
    +---------------------------------+""")
                elif (count % 10 == 1 and count != 1):
                    print(f"""
    | У меня ушла {count} попытка.    |
    +---------------------------------+""")
                break
            elif (otva == "равно") or (otva == "р" ) and my_n != a:
                print("""
    +---Бот-------------------------+
    | Я не верю что это ваше число! |
    +-------------------------------+""")
            else:
                print("""
    Ошибка синтаксиса!""")
                
    elif choice == 2:
        print("""
    +------Угадывает-Игрок (Вы)------+""")
        b1, b2, count = 1, 80, 1
        otvb = randint(b1, b2)
        print(f"""    +---Бот-----------------------------+
    | Я загадал число от {b1} до {b2}        |
    +-----------------------------------+""")
        while True:
            my_n = int(input(f"""
    • Угадайте число, которое я загадал. {b1, b2} -> """))
            if my_n < otvb:
                print("""
    +---Бот-------------+
    | Моё число больше. |
    +-------------------+""")
                b1 = my_n
                count += 1
            elif my_n > otvb:
                print("""
    +---Бот-------------+
    | Моё число меньше. |
    +-------------------+""")
                b2 = my_n
                count += 1
            elif my_n == otvb:
                print("""
    +---Бот--------------------------+
    | Вы угадали моё число!          |""")
                if (count == 1):
                    print("""
    | С первого раза!!!              |
    +--------------------------------+""")
                elif (count == 2) or (count == 3) or (count == 4) or (count % 10 == 2) or (count % 10 == 3) or (count % 10 == 4):
                    print(f"""
    | Всего лишь за {count} попытки! |
    +--------------------------------+""")
                elif (count == 5) or (count == 6) or (count == 7) or (count == 8) or (count == 9) or (count % 10 == 5) or (count % 10 == 6) or (count % 10 == 7) or (count % 10 == 8) or (count % 10 == 9) or (count % 10 == 0): 
                    print(f"""
    | За {count} попыток!            |
    +--------------------------------+""")
                elif (count % 10 == 1 and count != 1):
                    print(f"""
    | У вас ушла {count} попытка     |
    +--------------------------------+""")
                break


# QUADROFUNCTION


def quadroFunction():
    print("""
    +---Бот--------------+
    | Определение точек  |
    | графика ax²+bx+c   |
    +--------------------+""")
    a = int(input("    • Введите коэф. a: "))
    b = int(input("    • Введите коэф. b: "))
    c = int(input("    • Введите коэф. c: "))
        
    print(f"""
    +---Бот------------------------+
    | Ваша функция: {a}x²+{b}x+{c} |
    +------------------------------+""")
    print("Точки для графика (-10.0, +10.0):")
    
    st = -10
    stp = st - (2*st)
    result = 0
    mn = 999_999
    mx = 0
    x = []
    y = []
    while st < stp:
        print(f"    y({round(st, 2)}) = {a}*{round(st, 2)}²+{b}*{round(st, 2)}+{c} = {round(((a*(st**2))+(b*st)+c), 2)}", "- целое число" if round(((a*(st**2))+(b*st)+c), 2).is_integer() else "")
        result = round(((a*(st**2))+(b*st)+c), 2)
        
        if result <= mn:
            mn = result
            stmn = st
        if result > mx:
            mx = result
            stmx = st
            
        #x.append(round(st, 2))
        #y.append(result)
        st += 0.1
        
    print(f"""
    +---Бот---------------------------------------+
    | Минимальная точка: y({round(stmn, 2)})={mn} |
    +---------------------------------------------+""")
    print(f"""
    +---Бот----------------------------------------+
    | Максимальная точка: y({round(stmx, 2)})={mx} |
    +----------------------------------------------+""")


# QUARTER


def quarter():
    print("""
    +---Бот----------------------+
    | Напишите точки и узнайте,  |
    | в каких они четвертях      |
    | на координатной плоскости. |
    +----------------------------+
    """)
    x, y = map(int, input(f"    • Координаты A (через пробел x2): ").split())
    x1, y1 = map(int, input(f"    • Координаты B (через пробел x2): ").split())
    print(f"    Точка A {x, y}\n    Точка B {x1, y1}")
    
    if ((x > 0) and (y > 0)) and ((x1 > 0) and (y1 > 0)):
        print(f"""
    +---Бот---------------------------+
    | Точка A находится в 1 четверти  |
    | и точка B  в 1 четверти         |
    +---------------------------------+""")
    elif ((x < 0) and (y < 0)) and ((x1 < 0) and (y1 < 0)):
        print(f"""
    +---Бот---------------------------+
    | Точка A находится в 3 четверти  |
    | и точка B в 3 четверти          |
    +---------------------------------+""")  
    elif ((x > 0) and (y > 0)) and ((x1 < 0) and (y1 < 0)):
        print(f"""
    +---Бот---------------------------+
    | Точка A находится в 1 четверти, |
    | а точка B в 3 четверти          |
    +---------------------------------+""")
    elif ((x < 0) and (y < 0)) and ((x1 > 0) and (y1 > 0)):
        print(f"""
    +---Бот---------------------------+
    | Точка A находится в 3 четверти, |
    | а точка B в 1 четверти          |
    +---------------------------------+""")
    elif ((x > 0) and (y < 0)) and ((x1 > 0) and (y1 < 0)):
        print(f"""
    +---Бот---------------------------+
    | Точка A находится во 2 четверти | 
    | и точка B во 2 четверти         |
    +---------------------------------+""")
    elif ((x > 0) and (y > 0)) and ((x1 > 0) and (y1 < 0)):
        print(f"""
    +---Бот---------------------------+
    | Точка A находится в 1 четверти, |
    | а точка B во 2 четверти         |
    +---------------------------------+""")
    elif ((x > 0) and (y < 0)) and ((x1 > 0) and (y1 > 0)):
        print(f"""
    +---Бот---------------------------+
    | Точка A находится во 2 четверти,|
    | а точка B в 1 четверти          |
    +---------------------------------+""")
    elif ((x < 0) and (y > 0)) and ((x1 < 0) and (y1 > 0)):
        print(f"""
    +---Бот---------------------------+
    | Точка A находится в 4 четверти  |
    | и точка B в 4 четверти          |
    +---------------------------------+""")
    elif ((x < 0) and (y > 0)) and ((x1 > 0) and (y1 > 0)):
        print(f"""
    +---Бот---------------------------+
    | Точка A находится в 4 четверти, |
    | а точка B в 1 четверти          |
    +---------------------------------+""")
    elif ((x > 0) and (y > 0)) and ((x1 < 0) and (y1 > 0)):
        print(f"""
    +---Бот---------------------------+
    | Точка A находится в 1 четверти, |
    | а точка B в 4 четверти          |
    +---------------------------------+""")
        
        
    elif ((x < 0) and (y > 0)) and ((x1 < 0) and (y1 < 0)):
        print(f"""
    +---Бот----------------------------+
    | Точка A находится во 2 четверти, | 
    | а точка B в 3 четверти           |
    +----------------------------------+""")
    elif ((x < 0) and (y < 0)) and ((x1 < 0) and (y1 > 0)):
        print(f"""
    +---Бот---------------------------+
    | Точка A находится в 3 четверти, |
    | а точка B в 4 четверти          |
    +---------------------------------+""")
    elif ((x < 0) and (y > 0)) and ((x1 > 0) and (y1 < 0)):
        print(f"""
    +---Бот---------------------------+
    | Точка A находится в 4 четверти, |
    | а точка B во 2 четверти         |
    +---------------------------------+""")
    elif ((x > 0) and (y < 0)) and ((x1 < 0) and (y1 > 0)):
        print(f"""
    +---Бот---------------------------+
    | Точка A находится во 2 четверти,| 
    | а точка B в 4 четверти          |
    +---------------------------------+""")
    elif ((x > 0) and (y < 0)) and ((x1 < 0) and (y1 < 0)):
        print(f"""
    +---Бот---------------------------+
    | Точка A находится во 2 четверти,| 
    | а точка B в 3 четверти          |
    +---------------------------------+""")
    elif ((x < 0) and (y < 0)) and ((x1 > 0) and (y1 < 0)):
        print(f"""
    +---Бот---------------------------+
    | Точка A находится в 3 четверти, |
    | а точка B во 2 четверти         |
    +---------------------------------+""")
    

# TIME


def time():
    print("""
    +---Бот--------------------+
    | 1. Преобазование секунд  |
    |    в формат: дд:чч:мм:сс |
    | 2. Выход                 |
    +--------------------------+""")
    while True:
        choice = int(input("    • Ввберите действие -> "))
        if choice == 1:
            time = int(input("\n    • Напишите некоторое кол-во секунд: "))
            
            days = time // 86400
            hours = (time % 86400) // 3600
            minutes = (time % 3600) // 60
            seconds = time % 60
            
            if days > 0:
                print(f"""
    +---Бот--------------------------------+
    | Ваше время преобразованное           |
    | из секунд: {days}:{hours}:{minutes}:{seconds} (дд:чч:мм:сс) |
    +--------------------------------------+""")
            else:
                print(f"""
    +---Бот--------------------------------+
    | Ваше время преобразованное           |
    | из секунд: 00:{hours}:{minutes}:{seconds} (дд:чч:мм:сс) |
    +--------------------------------------+""")
        elif choice == 2:
            print("""
    +---Бот--------+
    | До свидания! |
    +--------------+""")
            break
        elif choice > 2:
            print("""
    +---Бот--------------+
    | Некоректный выбор! |
    +--------------------+""")


# YEP
    
    
def yep():
    print("\n    ------Created in 19.11.2024------")
    print("    Some random micro-programms")
    
    b = randint(0, 20)
    c = randint(0, 20)
        
    x = randint(1, 20)
    y = randint(1, 20)
    
    factorial = 1
    D = 0
    
    print(f"""
    b={b}, c={c}""")
    
    if b > x and c > y:
        print("""
    v    v""")
    elif b < x and c < y:
        print("""
    ^    ^""")
    elif b > x and c < y:
        print("""
    v    ^""")
    elif b < x and c > y:
        print("""
    ^    v""")
        
    print(f"""
    x={x}, y={y}""")
    
    if b > x and c > y:
        print("^v^v^v^v^")
        print(b,">", x)
        print(c,">", y)
    elif b < x and c < y:
        print("^v^v^v^v^")
        print(b,"<", x)
        print(c,"<", y)
    elif b > x and c < y:
        print("^v^v^v^v^")
        print(b,">", x)
        print(c,"<", y)
    elif b < x and c > y:
        print("^v^v^v^v^")
        print(b,"<", x)
        print(c,">", y)
    elif b == x and c > y:
        print("^v^v^v^v^")
        print(b,"=", x)
        print(c,">", y)
    elif b == x and c < y:
        print("^v^v^v^v^")
        print(b,"=", x)
        print(c,"<", y)
    elif b > x and c == y:
        print("^v^v^v^v^")
        print(b,">", x)
        print(c,"=", y)
    elif b < x and c == y:
        print("^v^v^v^v^")
        print(b,"<", x)
        print(c,"=", y)
    elif b == x and c == y:
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_")
        print(b,"=", x)
        print(c,"=", y)
        print("OHHHH MYYY GOOOOOOOOOD")
    
    print("-----------------------------")
    
    if c != 0:
        print("b / c =", b/c)
    else:
        print("b нельзя разделить на c")
    if b != 0:
        print("c / b =", c/b)
    else:
        print("c нельзя раздель на b")
    if y != 0:
        print("x / y =", x/y)
    else:
        print("x нельзя разделить на y")
    if x != 0:
        print("y / x =", y/x)
    else:
        print("y нельзя разделить на x")
    if b != 0:
        print("y / b =", y/b)
    else:
        print("y нельзя разделить на b")
    if c != 0:
        print("y / c =", y/c)
    else:
        print("y нельзя разделить на c")
    if b != 0:
        print("x / b =", x/b)
    else:
        print("x нельзя разделить на b")
    if c != 0:
        print("x / c =", x/c)
    else:
        print("x нельзя разделить на c")
    
    if b == x and c == y:
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_")
        print(b,"=", x)
        print(c,"=", y)
        print("OHHHH MYYY GOOOOOOOOOD")
    print("-----------------------------")
    
    print("b в степени c =", b**c)
    print("с в степени b =", c**b)
    print("x в степени y =", x**y)
    print("y в степени x =", y**x)
    print("b в степени x =", b**x)
    print("b в степени y =", b**y)
    print("c в степени x =", c**x)
    print("c в степени y =", c**y)
    
    
    if b == x and c == y:
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_")
        print(b,"=", x)
        print(c,"=", y)
        print("OHHHH MYYY GOOOOOOOOOD")
    print("-----------------------------")
    
    print("корень из b =", b**0.5)
    print("корень из c =", c**0.5)
    print("корень из x =", x**0.5)
    print("корень из y =", y**0.5)
    
    if b == x and c == y:
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_")
        print(b,"=", x)
        print(c,"=", y)
        print("OHHHH MYYY GOOOOOOOOOD")
    print("-----------------------------")
    
    for i in range(2, b+1):
        factorial *= i
    print("факториал b =", factorial)
    for j in range(2, c+1):
        factorial *= j
    print("факториал c =", factorial)
    for g in range(2, x+1):
        factorial *= g
    print("факториал x =", factorial)
    for f in range(2, y+1):
        factorial *= f
    print("факториал y =", factorial)
    
    if b == x and c == y:
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_")
        print(b,"=", x)
        print(c,"=", y)
        print("OHHHH MYYY GOOOOOOOOOD")
    print("-----------------------------")
    
    D = (c**2)-(4*b*x)
    print("Дискриминант b^2+c+x =", D)
    if D > 0:
        print("x1 =", (-c + (D**0.5) / 2*b))
        print("x2 =", (-c - (D**0.5) / 2*b))
    elif D == 0:
        print("x =", -(c / (2*b)))
    elif D < 0:
        print(" Нет корней")
    D = (x**2)-(4*c*y)
    print("Дискриминант c^2+x+y =", D)
    if D > 0:
        print("x1 =", (-x + (D**0.5) / 2*c))
        print("x2 =", (-x - (D**0.5) / 2*c))
    elif D == 0:
        print("x =", -(x / (2*c)))
    elif D < 0:
        print(" Нет корней")
    D = (y**2)-(4*x*b)
    print("Дискриминант x^2+y+b =", D)
    if D > 0:
        print("x1 =", (-y + (D**0.5) / 2*x))
        print("x2 =", (-y - (D**0.5) / 2*x))
    elif D == 0:
        print("x =", -(y / (2*x)))
    elif D < 0:
        print(" Нет корней")
    D = (c**2)-(4*b*x)
    print("Дискриминант y^2+b+c =", D)
    if D > 0:
        print("x1 =", (-b + (D**0.5) / 2*y))
        print("x2 =", (-b - (D**0.5) / 2*y))
    elif D == 0:
        print("x =", -(b / (2*y)))
    elif D < 0:
        print(" Нет корней")
    
    if b == x and c == y:
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_")
        print(b,"=", x)
        print(c,"=", y)
        print("OHHHH MYYY GOOOOOOOOOD")
    print("-----------------------------")
    
    print("a =", b)
    print("Площадь квадрата =", b**2)
    print("a =", c)
    print("Площадь квадрата =", c**2)
    print("a =", x)
    print("Площадь квадрата =", x**2)
    print("a =", y)
    print("Площадь квадрата =", y**2)
    print("a =", b, "b =", c)
    print("Площадь прямоугольника =", b*c)
    print("a =", c, "b =", x)
    print("Площадь прямоугольника =", c*x)
    print("a =", x, "b =", y)
    print("Площадь прямоугольника =", x*y)
    print("a =", y, "b =", b)
    print("Площадь прямоугольника =", y*b)
    
    if b == x and c == y:
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_")
        print(b,"=", x)
        print(c,"=", y)
        print("OHHHH MYYY GOOOOOOOOOD")
    print("-----------------------------")
    #print(" ")
    #t = int(input("Запиши любое число: "))
    #m = int(input("Запишите на сколько нулей влево/вправо сместится запятая: "))
    #if m == 1:
    #    m = 10
    #    print(t * m)
    #if m == -1:
    #    m = 10
    #    print(t / m)
    mn = list()
    for p in range(b, b*b+1):
        mn.append(p)
    sm = sum(mn)
    print(*mn, sep=" < ")
    print("-----------------------------")
    
    files = ["1: config", "2: libraries", "3: logs", "4: mods", "5: world", "6: banned-ips.json", "7: banned-players.json", "8: eula.txt", "9: forge-1.12.2-14.23.5.2860.jar", "10: minecraft_server-1.12.2.jar", "11: ops.json", "12: server.properties", "13: start.bat", "14: usercache.json", "15:whitelist.json"]
    for fi in files:
        print(fi)
        
    print("------------random------------")
    
    for o in range(14):
        print(files[randint(0,14)])
        
    print("------------------------------")
    
    d = pi
    print(d)
    
    print("------------------------------")
    
    ra = randint(0,3)
    rb = randint(0,3)
    rc = randint(0,3)
    rd = randint(0,3)
    re = randint(0,3)
    print(f"0-3:  {ra}, {rb}, {rc}, {rd}, {re}")
    print(" ")
    
    rtrue1 = randint(0,1)
    rtrue2 = randint(0,1)
    rtrue3 = randint(0,1)
    rfalse1 = randint(0,1)
    rfalse2 = randint(0,1)
    rfalse3 = randint(0,1)
    print(f"0-1:  {rtrue1}, {rtrue2}, {rtrue3}, {rfalse1}, {rfalse2}, {rfalse3}")
    print(" ")
    
    figure = ["1: circle", "2: tringle", "3: squad", "4: cross"]
    for ca in figure:
        print(ca)
        
    print("----random----")
    
    for ca in range(0,4):
        print(figure[randint(0,3)])
    
    
    
    
    print("------------------------------")
    print("Collection of coins (random) for 'Проезд на маршрутке на 2025 год'")
    
    rubles = [1, 2, 5, 10]
    variant = randint(1, 5)
    print("")
    print("Variant #", variant, ":", sep="")
    print("")
    
    if variant == 1:
        result = rubles[0]*33
        print("1*33 -> ", result, " rubles", sep="")
    elif variant == 2:
        result = rubles[1]*16+rubles[0]
        print("(2*16)+1 -> ", result, " rubles", sep="")
    elif variant == 3:
        result = rubles[2]*6+rubles[1]+rubles[0]
        print("(5*6)+2+1 -> ", result, " rubles", sep="")
    elif variant == 4:
        result = rubles[3]*3+rubles[1]+rubles[0]
        print("(10*3)+2+1 -> ", result, " rubles", sep="")
    elif variant == 5:
        result = rubles[3]*3+rubles[0]*3
        print("(10*3)+(1*3) -> ", result, " rubles", sep="")
        
    
    
    print(" ")
    print("-----------ALPHABET-------------")
    print("17.12.25")
    print("")
    
    counter = 0
    alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з']
    alphabet2 = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з']
        
    print("Building the alphabet...")
            
    while True:
        random.shuffle(alphabet2)
        counter += 1
        ##print("Building the alphabet: Attempt #", counter, sep="")
        if alphabet2 == alphabet:
            print("\n\nWe built the alphabet in ", counter, " attempts!!!\n\nAlphabet2: ", alphabet2, sep="")
            break

if __name__ == "__main__":
    collection()
