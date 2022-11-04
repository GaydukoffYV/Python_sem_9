import rational as op
from datetime import datetime as dt


def res(first, select, second):
    operatione = select
    firstnum = first
    secondnum = second
    if  operatione == '+':
        res = firstnum + secondnum
        result = round(res, 3)
        return result
    elif operatione == '-':
        res = firstnum - secondnum
        result = round(res, 3)
        return result
    elif operatione == '*':
        res = firstnum * secondnum
        result = round(res, 3)
        return result
    elif operatione == '/':
        res = firstnum / secondnum
        result = round(res, 3)
        return result
    else:
        print('Недопустимый символ')

def mainterminal(x, selectoperation, y, id):
    x = float(x.replace(',', '.'))
    oper = selectoperation
    y = float(y.replace(',', '.'))
    res = op.res(x, oper, y)
    time = dt.now().strftime('%d.%m.%Y %H:%M:%S')
    with open('results.json', 'a') as data:
        data.write(f'{time} {id} : Результат {x} {oper} {y} = {res}\n')
    print(f'Результат {x} {oper} {y} = {res}\n')
    return res