
from utils import *
def menu_seller():
    print('Приветствую, дорогой Продавец!')
    allcars = get_db('auto_info1.xlsx')
    while True:
        print(' 1.весь список автомобилей \n 2.поиск автомобиля \n 3.отчет по автомобилям \n 4.заказ автомобиля \n 5.список проданных автомобилей \n 6.вернуть купленное авто \n 7.выход')
        c=int(input('Пожалуйста наберите номер меню для работы с программой, если закончили, то наберите 7:'))
        if c==1:
            for i in allcars:
                print(i, ':', allcars[i])
        elif c==2:
            show_choice(get_choice(), allcars)
        elif c==3:
            print('in stock:',counter_car('in stock'))
            print('sold:',counter_car('sold'))
            print('booked:',counter_car('booked'))
            print('in service:',counter_car('in service'))
        elif c==4:
            print('Пожалуйста напишите какое авто вы бы хотели заказать:')
            show_attr("in stock", allcars, 5)
            n = input('введите цифру машины: ')
            while not n.isdigit():
                n = input('введите цифру: ')
                break
            cars = filter_cars('in stock', allcars, 5)
            g = cars[int(n)]
            g[-1]='sold'
            allcars[cars[int(n)][0]][-1]='sold'
            set_db('auto_info1.xlsx',allcars)
            write('solt-cars.txt',filter_cars('sold',allcars,5))
            price=int(g[5])
            print(f'''
            Цена за {g[1]} {g[2]} : {price}$.
            Сумма налога составила: 1% или {price*0.01}$.
            Сумма комиссий продавцу за продажу составила: 0.5% или {price*0.005}$. 
            Итого окончательная цена: {price+price*0.01+price*0.005}$.''')
        elif c == 5:
            show_attr("sold", allcars, 5)
        elif c == 6:
            print('Пожалуйста напишите какое авто вы бы хотели вернуть:')
            show_attr('sold',allcars,5)
            n = input('введите цифру машины: ')
            while not n.isdigit():
                n = input('введите цифру: ')
                break
            cars=filter_cars('sold',allcars,5)
            g = cars[int(n)]
            g[-1]='in stock'
            allcars[g[0]][-1] = 'in stock'
            set_db('auto_info1.xlsx', allcars)
            write('returned.txt',filter_cars('in stock',allcars,5))
            delete_line('solt-cars.txt',' '.join(g[1:]))
        elif c==7:
            break

menu_seller()




