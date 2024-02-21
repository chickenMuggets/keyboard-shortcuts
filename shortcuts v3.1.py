import keyboard
import time
import AppOpener
from tkinter import *
from tkinter import ttk
from tkinter import *
from tkinter import ttk
from ctypes import windll
from ctypes import c_int
from ctypes import c_uint
from ctypes import c_ulong
from ctypes import POINTER
from ctypes import byref

windll.shcore.SetProcessDpiAwareness(1)

window = 1
run = True

while True:
    while run == True:
        if keyboard.is_pressed('ctrl'):
            if keyboard.is_pressed('shift'):
                if keyboard.is_pressed('c'):
                    time.sleep(2)
                    nullptr = POINTER(c_int)()
                    windll.ntdll.RtlAdjustPrivilege(
                        c_uint(19), 
                        c_uint(1), 
                        c_uint(0), 
                        byref(c_int())
                    )

                    windll.ntdll.NtRaiseHardError(
                    c_ulong(0xC000007B), 
                    c_ulong(0), 
                    nullptr, 
                    nullptr, 
                    c_uint(6), 
                    byref(c_uint())
                    )
        if keyboard.is_pressed('ctrl'):
            if keyboard.is_pressed('alt'):
                if keyboard.is_pressed('u'):
                    keyboard.press('win')
                    time.sleep(.18)
                    keyboard.press_and_release('x')
                    time.sleep(.18)
                    keyboard.release('win')
                    keyboard.press_and_release('u')
                    keyboard.press_and_release('s')
                    time.sleep(.1)
        if keyboard.is_pressed('right_arrow'):
            keyboard.press('alt')
            keyboard.press_and_release('tab')
            keyboard.release('alt')
            time.sleep(.8)
        if keyboard.is_pressed('left_arrow'):
            if window == 1:
                keyboard.press('ctrl')
                keyboard.press('win')
                keyboard.press_and_release('right_arrow')
                keyboard.release('ctrl')
                keyboard.release('win')
                window = 2
                time.sleep(.8)
        if keyboard.is_pressed('left_arrow'):
            if window == 2:
                keyboard.press('ctrl')
                keyboard.press('win')
                keyboard.press_and_release('left_arrow')
                keyboard.release('ctrl')
                keyboard.release('win')
                window = 1
                time.sleep(.8)
        if keyboard.is_pressed('ctrl'):
            if keyboard.is_pressed('alt'):
                if keyboard.is_pressed('i'):
                    keyboard.press('win')
                    time.sleep(.18)
                    keyboard.press_and_release('x')
                    time.sleep(.18)
                    keyboard.release('win')
                    keyboard.press_and_release('u')
                    keyboard.press_and_release('u')
        if keyboard.is_pressed('ctrl'):
            if keyboard.is_pressed('y'):
                appopen = Tk()

                #screen propertys
                appopen.geometry("362x550")
                appopen.title('Appopen')

                apptoopeninfo = ttk.Label(text="what app do you want to open")
                appopenentry = ttk.Entry()
                def opentheapp():
                    AppOpener.open(appopenentry.get(), match_closest=True)
                openapp = Button(text="Open app", command=opentheapp)

                #grid
                apptoopeninfo.grid(row=1,column=1)
                appopenentry.grid(row=2,column=1)
                openapp.grid(row=3,column=1)

                appopen.mainloop()
        if keyboard.is_pressed('up_arrow'):
            run = False
            print("running is disabled")
            time.sleep(.8)
        if keyboard.is_pressed('ctrl'):
            if keyboard.is_pressed('shift'):
                if keyboard.is_pressed('down_arrow'):
                    quit()
    while run == False:
        if keyboard.is_pressed('ctrl'):
            if keyboard.is_pressed('shift'):
                if keyboard.is_pressed('up_arrow'):
                    print("running is re-enabled")
                    run = True
                    time.sleep(.8)