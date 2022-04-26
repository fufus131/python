import pyautogui
n = input('Ведите Логин:')
while(n != 'fufus'):
    n = input('Неверный логин, введите логин:')
print('логин верный')
n2 = input('Ведите пароль:')
while(n2 != '7689'):
    n2 = input('Неверный пароль, введите пароль:')
print('Пароль верный')
pyautogui.alert(text='Вы успешно вошли в аккаунт')