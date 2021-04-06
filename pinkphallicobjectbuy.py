import pyautogui
import time

print("machine on")

pink_phallic_object_num = 43
run_script = "pls buy pinkphallicobject"

def pyautogui_cycle(script):
    pyautogui.typewrite(script, interval = 0.0225)
    pyautogui.press("enter")

while pink_phallic_object_num <= 418:
    finished_script = f"```{pink_phallic_object_num}th script successfully ran```"

    time.sleep(float(5.15))
    pyautogui_cycle(run_script)
    pyautogui_cycle(finished_script)
    print(f"bought the {pink_phallic_object_num}th dildo")
    pink_phallic_object_num += 1
