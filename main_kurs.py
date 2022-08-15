
import openpyxl as xl
from utils import*

while True:
    wb = xl.load_workbook('accounts.xlsx')
    sheet = wb.active
    a = []
    b = []
    c = []
    for cell in list(sheet.columns)[0][0:]:
        a.append(cell.value)
    for cell in list(sheet.columns)[1][0:]:
        b.append(cell.value)
    for cell in list(sheet.columns)[2][0:]:
        c.append(str(cell.value))
    print(a,b,c)
    ak = input('Введите аккаунт: ')
    if ak not in a:
        print('Извините, но мы не нашли такой тип аккаунта, пожалуйста повторите.')
    elif ak in a:
        while True:
            login = input('Введите логин')
            password = input('Введите пороль')
            if login not in b:
                print('Неверный логин, введите еще раз')
            elif password not in c:
                print('Неверный пороль,введите еще раз')
            elif password not in c and login not in b:
                print('неверный логин и пороль,введите еще раз')
            elif login in b[1] and password in c[1]:
                menu_seller()
            elif login in b[0] and c[0]:
                menu_director()
            elif login in b[2] and password in c[2]:
                menu_repairman()
print('Программа завершена!')
