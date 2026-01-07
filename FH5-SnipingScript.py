import keyboard
import time
import os
import sys
import win32gui

# ================= CONFIG =================
VENTANA_PERMITIDA = "Forza Horizon 5"
running = True
# ==========================================

def clear():
    os.system('cls')

def ventana_activa_es_fh5():
    hwnd = win32gui.GetForegroundWindow()
    titulo = win32gui.GetWindowText(hwnd)
    return VENTANA_PERMITIDA.lower() in titulo.lower()

def stop_script():
    global running
    running = False
    clear()
    print(f"Script detenido por seguridad.")
    sys.exit()

# ESC para detener todo
keyboard.add_hotkey('esc', stop_script)

clear()
timer = 0.0
counter = 0
start = 1

if start == 1:
    while running:
        clear()
        print(' ----------------------------------------------------------------------')
        print('|         Python FH5 Sniping Script (Dvix-Dev FORK 🍴)                 |')
        print('|                                                                      |')
        print('|   1- Deja preparado el coche seleccionado con el maximo precio       |')
        print('|   2- Ten la ventana de forza focuseada en los 5 segundos             |')
        print('|   3- Presiona ESC en cualquier momento para detener                  |')
        print('|                                                                      |')
        print('|      Buena suerte!                                                   |')
        print(' ----------------------------------------------------------------------')

        a = input('\nEmpezar el Script? s/n: ').lower()

        if a == 'n':
            stop_script()

        elif a == 's':
            clear()
            for i in range(5, -1, -1):
                if not ventana_activa_es_fh5():
                    stop_script()

                print('FOCUS A LA VENTANA!!\nSnipeando en:')
                print(f'{i} segundos')
                time.sleep(1)
                clear()

            # Loop principal de sniping
            while running:
                # Comprobar foco ANTES de enviar inputs
                if not ventana_activa_es_fh5():
                    stop_script()

                counter += 1
                timer += 2.33
                minuteCounter = timer / 60

                clear()
                print(f'Intentos: {counter} veces')
                print(f'{round(timer, 1)} segundos ({round(minuteCounter, 1)} minutos)')

                keyboard.press_and_release('enter')
                time.sleep(0.25)
                keyboard.press_and_release('enter')
                time.sleep(0.78)
                keyboard.press_and_release('y')
                time.sleep(0.25)
                keyboard.press_and_release('down')
                time.sleep(0.1)
                keyboard.press_and_release('enter')
                time.sleep(0.2)
                keyboard.press_and_release('enter')
                keyboard.press_and_release('esc')
                time.sleep(0.75)

        else:
            continue
