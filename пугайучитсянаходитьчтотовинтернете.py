import pyautogui
import time
n = input("Что хотитие найти?")
pyautogui.moveTo(167, 744)
pyautogui.click()
pyautogui.moveTo(1046, 10)
pyautogui.click()
pyautogui.moveTo(167, 57)
pyautogui.click()
pyautogui.write(n)
pyautogui.press('enter')