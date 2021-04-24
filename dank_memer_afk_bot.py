'''
Copyright (©) 2021 Kiet Pham <kiet.riley2005@gmail.com>
This software/program has a copyright license, more information is in the 'LICENSE' file
IF YOU WANT TO USE/COPY/MODIFY/REPRODUCE/RE-DISTRIBUTE THIS PROGRAM, YOU MUST INCLUDE A COPY OF THE LICENSE

Author Name: Kiet Pham
Author Contact: kiet.riley2005@gmail.com
Discord: CaptainVietnam6#7932
Discord Server: https://discord.gg/3z76p8H5yj
GitHub: https://github.com/CaptainVietnam6
Instagram: @itz_kietttttttttt
Program Status: FINALISED, ABANDONED
'''

import pyautogui
import time
import random

machine_on_message = "Machine on, starting in 5 seconds"
print(machine_on_message)
pyautogui.typewrite(machine_on_message)
pyautogui.press("enter")
on_countdown = 5
time.sleep(float(0.5))
for i in range(5):
    send_on_countdown = f"starting in {on_countdown} seconds"
    print(f"starting in {on_countdown} seconds")
    pyautogui.typewrite(send_on_countdown)
    pyautogui.press("enter")
    on_countdown -= 1
    time.sleep(1)

'''SCRIPTS FOR PYAUTOGUI TO TYPE OUT'''

#DEPOSIT ALL SCRIPT:
deposit_script = "pls dep all"

#SELL ALL FISH SCRIPT:
sell_fish_script = "pls sell fish all"

#HIGHLOW SCRIPTS
#highlow print script:
highlow_script = "pls highlow"
#randomly picks high or low
highlow_responses = ["high", "low"]

#BEG SCRIPT:
beg_script = "pls beg"

#POSTMEME SCRIPT:
#postmeme print script:
postmeme_script = "pls pm"
#postmeme response script:
postmeme_responses = ["f", "r", "i", "c", "k"]

#FISHING SCRIPT:
fishing_script = "pls fish"

#HUNT SCRIPT
hunting_script = "pls hunt"

'''DEFINE ALL RUNS'''

def pyautogui_cycle(script):
    pyautogui.typewrite(script, interval = 0.0225)
    pyautogui.press("enter")

def deposit_script_run():
    pyautogui_cycle(deposit_script)
    print("deposited all money in wallet")

def sell_fish_script_run():
    pyautogui_cycle(sell_fish_script)
    print("sold all fishes in inventory")

def highlow_script_run():
    pyautogui_cycle(highlow_script)
    print("highlow starter script ran")

def highlow_reply_run():
    pyautogui_cycle(highlow_reply)
    print("highlow reply script ran")

def beg_script_run():
    pyautogui_cycle(beg_script)
    print("beg script ran")

def postmeme_script_run():
    pyautogui_cycle(postmeme_script)
    print("post meme starter script ran")

def postmeme_reply_run():
    pyautogui_cycle(postmeme_reply)
    print("post meme reply script ran")

def fishing_script_run():
    pyautogui_cycle(fishing_script)
    print("fishing script ran")

def hunting_script_run():
    pyautogui_cycle(hunting_script)
    print("hunting script ran")

def main_run():
    run_num = 0
    while run_num < 460:
        global highlow_reply
        global postmeme_reply
        highlow_reply = random.choice(highlow_responses)
        postmeme_reply = random.choice(postmeme_responses)

        hunting_script_run()
        time.sleep(1)
        highlow_script_run()
        time.sleep(float(2.5))
        highlow_reply_run()
        time.sleep(6)
        fishing_script_run()
        time.sleep(5)
        postmeme_script_run()
        time.sleep(float(2.5))
        postmeme_reply_run()
        time.sleep(float(2.5))
        beg_script_run()
        time.sleep(11)
        highlow_script_run()
        time.sleep(float(2.5))
        highlow_reply_run()
        time.sleep(5)
        time.sleep(24)
        highlow_script_run()
        time.sleep(float(2.5))
        highlow_reply_run()
        time.sleep(float(7.5))
        beg_script_run()
        time.sleep(float(7.5))
        fishing_script_run()
        time.sleep(1)
        hunting_script_run()
        time.sleep(5)
        highlow_script_run()
        time.sleep(float(2.5))
        highlow_reply_run()
        time.sleep(float(2.5))
        postmeme_script_run()
        time.sleep(float(2.5))
        postmeme_reply_run()
        time.sleep(15)
        highlow_script_run()
        time.sleep(float(2.5))
        highlow_reply_run()
        time.sleep(float(7.5))
        beg_script_run()
        time.sleep(float(12.5))
        highlow_script_run()
        time.sleep(float(2.5))
        highlow_reply_run()
        time.sleep(5)
        deposit_script_run()
        time.sleep(5)
        time.sleep(10)
        
        run_num = run_num + 1
        print(f"{run_num}th cycle complete")
        
main_run()
