vibiri = input('Выберите+,-,*,/')
while vibiri !="exit":
    if vibiri == 'kraborifma':
        krabob = input('Ведите любое слово')
        print('Крабо' + krabob)
    if vibiri == 'chepuha':
       kto = input('Кто?')
       skem = input('С кем')
       kogda = input('Когда?')
       gde = input('Где?')
       chto = input('Что случилсь?')
       end = input('Чем закончилось?')
       print(kto + "," + skem + "," + kogda + "," + gde + "," + chto + "," + end)
    if vibiri == '+':
       pervoe = input('Введите первое слогаемое')
       pervoe = int(pervoe)
       vtoroe = input('Введите второе слогаемое')
       vtoroe = int(vtoroe)
       print(pervoe + vtoroe)
    if vibiri == '-':
        pervoe = input('Введите уменьшаемое')
        pervoe = int(pervoe)
        vtoroe = input('Введите уменьшитель')
        vtoroe = int(vtoroe)
        print(pervoe - vtoroe)
    if vibiri == '*':
        pervoe = input('Введите умножаемое')
        pervoe = int(pervoe)
        vtoroe = input('Введите множитель')
        vtoroe = int(vtoroe)
        print(pervoe * vtoroe)
    if vibiri == '/':
        pervoe = input('Введите делимое')
        pervoe = int(pervoe)
        vtoroe = input('Введите делитель')
        vtoroe = int(vtoroe)
        print(pervoe / vtoroe)
    vibiri = input('Выберите +,-,*,/')