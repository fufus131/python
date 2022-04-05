import pyautogui
im = input('Ведите име')
fa = input('Ведите фамилию')
pyautogui.alert(text= 'Hello' + ' '+ im + ',' + fa)