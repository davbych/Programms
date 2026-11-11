#---IMPORTS-----------------------------------------------#
import pyautogui as pag
import pydirectinput as pdi
import time

#---BODY--------------------------------------------------#
def script1():
    pass
def script2():
    for i in range(5,0,-1):
        print("Time left:", i)
        time.sleep(1)
    for _ in range(1, 43+1):
        pdi.press("end")
        for _ in range(1, 4+1):
            pdi.press("left")
        for _ in range(1, 3+1):
            pdi.press("backspace")
        pdi.press("9")
        pdi.press(".")
        pdi.press("7")
        pdi.press(".")
        pdi.press("1")
        pdi.press("down")
def script3():
    pdi.keyDown("alt")
    pdi.keyDown("tab")
    time.sleep(1)
    pdi.keyUp("alt")
    pdi.keyUp("tab")
def script4(): #Minecraft: Встать по центру круга с радиусом 3 и смотреть ЧЁТКО вниз (0.0; 90.0)
    pause = 0.3
    script3() #Alt + Tab
    for i in range(10):
        for i in range(4):
            time.sleep(0.5)
            pag.moveRel(0, -170, 0.2)
            pag.mouseDown()
            time.sleep(pause)
            pag.mouseUp()

            pag.moveRel(55, -5, 0.2)
            pag.mouseDown()
            time.sleep(pause)
            pag.mouseUp()

            pag.moveRel(-70, 30, 0.2)
            pag.mouseDown()
            time.sleep(pause)
            pag.mouseUp()

            pag.moveRel(70, 0, 0.2)
            pag.mouseDown()
            time.sleep(pause)
            pag.mouseUp()

            pag.moveRel(50, -20, 0.2)
            pag.mouseDown()
            time.sleep(pause)
            pag.mouseUp()

            pag.moveRel(-110, 60, 0.2)
            pag.mouseDown()
            time.sleep(pause)
            pag.mouseUp()

            pag.moveRel(110, 0, 0.2)
            pag.mouseDown()
            time.sleep(pause)
            pag.mouseUp()

            pag.moveRel(60, -40, 0.2)
            pag.mouseDown()
            time.sleep(pause)
            pag.mouseUp()

            pag.moveRel(15, -25, 0.2)
            pag.mouseDown()
            time.sleep(pause)
            pag.mouseUp()

            pag.moveRel(60, 200, 0.2)#x:-185; y:185
        pag.mouseDown()
        time.sleep(pause)
        pag.mouseUp()
def script5():
    minetime = 0.5
    script3() #Alt + Tab
    for i in range(20):
        pag.mouseDown()
        time.sleep(minetime)
        pag.mouseUp()

        pag.moveRel(0, 50, duration=0.5)
        pag.mouseDown()
        time.sleep(minetime)
        pag.mouseUp()

        pag.moveRel(0, -90, duration=0.5)
        pag.mouseDown()
        time.sleep(minetime)
        pag.mouseUp()

        pag.moveRel(0, -40, duration=0.5)
        pag.mouseDown()
        time.sleep(minetime)
        pag.mouseUp()

        pag.moveRel(0, -15, duration=0.5)
        pag.mouseDown()
        time.sleep(minetime)
        pag.mouseUp()

        pag.moveRel(0, 0, duration=0.5)
        pag.mouseDown()
        time.sleep(minetime)
        pag.mouseUp()

        pag.moveRel(0, 96, duration=0.5)
        pag.keyDown("w")
        time.sleep(0.3)
        pag.keyUp("w")
def script6():
    pass

def restart():
    #pdi.click(1400, 14) #Monitor - 1920 x 1080
    #pdi.click(2200, 20) #Monitor - 2560 x 1440
    return 


pdi.PAUSE = 0.05
pdi.FAILSAFE = True
scripts_list = [ #False - скрипт не активен, True - скрипт активен
    ("Скрипт 1", "Действие 1", script1, True),
    ("Скрипт 2", "9.7.1", script2, False),
    ("Скрипт 3", "Alt + Tab", script3, True),
    ("Скрипт 4", "Minecraft (mine 3x3)", script4, True),
    ("Скрипт 5", "Minecraft (tunnel 1x6)", script5, True),
    ("Скрипт 6", "Minecraft (craft)", script6, True),
]

def ahk():
    active = [(name, desc, func) for name, desc, func, active in scripts_list if active]
    while True:
        print("\n+---Davby's AHK scripts---")
        for i, (name, desc, _) in enumerate(active, 1):
            print(f"| {i}. {name} - {desc}")
        print(f"| {len(active) + 1}. Выключить программу")
        print(f"| {len(active) + 2}. Перезапустить программу\n+", "-" * 25, sep="")
        pdi.click(1500, 370)

        try:
            choice = int(input("Введите номер пункта: "))
        except ValueError:
            print("\n+---Davby's AHK scripts---")
            print(f"| Введённые данные не являются цифрой!\n+", "-" * 25, sep="")
            continue

        if 1 <= choice <= len(active):
            name, desc, func = active[choice - 1]
            print("\n+---Davby's AHK scripts---")
            print(f"| Выполнение {name} ({desc})...\n+", "-" * 25, sep="")
            try:
                func()
            except Exception as e:
                print("\n+---Davby's AHK scripts---")
                print(f"| Выполнение скрипта остановлено из-за ошибки: {e}\n+", "-" * 25, sep="")
        elif choice == len(active) + 1:
            print("\n+---Davby's AHK scripts---")
            print("| Завершение работы программы...\n+", "-" * 25, sep="")
            break
        elif choice == len(active) + 2:
            print("\n+---Davby's AHK scripts---")
            print(f"| Перезапуск программы...\n+", "-" * 25, sep="")
            time.sleep(1)
            restart()
        else:
            print("\n+---Davby's AHK scripts---")
            print(f"| Пункт ({choice}) не существует.\n+", "-" * 25, sep="")
            continue

#---ACTIONS----------------------------------------------#
if __name__ == '__main__':
    ahk()
