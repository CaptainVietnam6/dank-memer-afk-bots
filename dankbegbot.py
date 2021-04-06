import pyautogui
import time

print("machine on, starting in 3 seconds")
time.sleep(3)

run_cycle = 0
gamble_script = "pls gamble 100"
beg_script = "pls beg"

def pyautogui_cycle(script):
    pyautogui.typewrite(script, interval = 0.0225)
    pyautogui.press("enter")

def gamble_script_run():
    pyautogui_cycle(gamble_script)

def beg_script_run():
    pyautogui_cycle(beg_script)

while run_cycle < 480:
    time.sleep(float(0.5))
    for i in range(5):
        gamble_script_run()
        time.sleep(float(8.25))
    time.sleep(4)
    beg_script_run()
