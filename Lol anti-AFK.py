import pyautogui
import time
import keyboard

# it waits for 2 sec. for the start
time.sleep(2)

try:
    while True:
        # 'q' for quit
        if keyboard.is_pressed('q'):
            print("Code End.")
            break
        
        pyautogui.moveTo(1119, 420)
        pyautogui.click(button="right")
        time.sleep(0.1)

        pyautogui.moveTo(871, 593)
        pyautogui.click(button="right")
        time.sleep(0.1)

except Exception as e:
    print(f"Problem: {e}")
