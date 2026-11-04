import pyautogui as pag
import pydirectinput as pdi
import time

#------------------------FUNCTIONS------------------------#
##------system_functions------##
pag.PAUSE = 0.05
pag.FAILSAFE = True

def longStart():
    while True:
        print("\nDavby's AHK script\n"
              "1. Action1\n"
              "2. Action2\n"
              "3. Tonnel(1x6)\n"
              "4. Pos. Mouse\n"
              "5. (EMPTY)\n"
              "6. Exit\n")
        choice = input("Enter your choice: ")
        if choice == "1":
            action1()
        elif choice == "2":
            action2()
        elif choice == "3":
            tonnel1x6()
        elif choice == "4":
            posmouse()
        elif choice == "5":
            pass
        elif choice == "6":
            break
        else:
            print("\nInvalid choice!")

##------script_funct1ions------##
def action1():
    pass
def action2():
    for i in range(5,0,-1):
        print("Time left:", i)
        time.sleep(1)
    for _ in range(1, 33+1):
        pdi.press("home")
        pdi.press("right")
        pdi.press("backspace")
        pdi.keyDown("shift")
        pdi.press("d")
        pdi.keyUp("shift")
        for _ in range(1, 11+1):
            pdi.press("right")
        for _ in range(1, 5+1):
            pdi.press("backspace")
        pdi.press("9")
        pdi.press(".")
        pdi.press("7")
        pdi.press(".")
        pdi.press("1")
        pdi.press("down")
def altab():
    pag.keyDown("alt")
    pag.keyDown("tab")
    time.sleep(0.1)
    pag.keyUp("alt")
    pag.keyUp("tab")
def posmouse():
    print(f"###\nMouse's position: {pag.position()} \n###")
def shahta3x3(): #Minecraft: Встать по центру круга с радиусом 3 и смотреть ЧЁТКО вниз (0.0; 90.0)
    pause = 0.3
    altab()
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
def tonnel1x6():
    minetime = 0.5
    altab()

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
def craft():
    pass

#------------------------ACTIONS------------------------#
longStart()
#shahta3x3()
#tonnel1x6()