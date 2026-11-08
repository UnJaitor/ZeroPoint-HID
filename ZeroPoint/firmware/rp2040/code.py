import board
import busio
import usb_hid
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS # Asume PCs en inglés, cambia a layout_es si lo necesitas

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
uart = busio.UART(board.GP4, board.GP5, baudrate=115200, timeout=0.1)

print("RP2040 BadUSB Listo. Esperando a la Web...")

while True:
    if uart.in_waiting > 0:
        raw_data = uart.read(uart.in_waiting)
        if raw_data:
            try:
                cmd = raw_data.decode('utf-8', 'ignore').strip()
                print("Recibido:", cmd)

                # Si el comando empieza por TXT:, escribe todo lo que va detrás simulando el teclado
                if cmd.startswith("TXT:"):
                    layout.write(cmd[4:])

                elif cmd.startswith("KEY:"):
                    tecla = cmd[4:]

                    if tecla == "ENTER": kbd.send(Keycode.ENTER)
                    elif tecla == "TAB": kbd.send(Keycode.TAB)
                    elif tecla == "ESC": kbd.send(Keycode.ESCAPE)

                    # Windows (Win + R)
                    elif tecla == "GUI_R":
                        kbd.press(Keycode.WINDOWS, Keycode.R)
                        time.sleep(0.05)
                        kbd.release_all()

                    # macOS (Cmd + Espacio para abrir Spotlight)
                    elif tecla == "GUI_SPACE":
                        kbd.press(Keycode.GUI, Keycode.SPACEBAR)
                        time.sleep(0.05)
                        kbd.release_all()

                    # Linux / Ubuntu (Ctrl + Alt + T para abrir Terminal)
                    elif tecla == "CTRL_ALT_T":
                        kbd.press(Keycode.CONTROL, Keycode.ALT, Keycode.T)
                        time.sleep(0.05)
                        kbd.release_all()

                # Comandos de control estáticos
                elif cmd == "ATTACK_1":
                    kbd.press(Keycode.WINDOWS, Keycode.R)
                    time.sleep(0.05)
                    kbd.release_all()
                elif cmd == "PLAY":
                    kbd.send(Keycode.F5)
                elif cmd == "NEXT":
                    kbd.send(Keycode.RIGHT_ARROW)
                elif cmd == "PREV":
                    kbd.send(Keycode.LEFT_ARROW)

            except Exception as e:
                print("Error:", e)

    time.sleep(0.05)



# By: UnJaitor
# https://github.com/UnJaitor


# Distributed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) license.
# Non-Commercial: You cannot sell hardware kits or use this project for financial gain.
# ShareAlike: Any modification or derivative work must remain open-source under the same terms.
