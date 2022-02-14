import sys

a = input()
b = sys.argv[1:]
info = 'Справка: Для сравнения чисел должны быть присвоены числовые значения двум аргументам'

def comparing():
    """Comparing numbers"""
    if float(a) > float(b):
        print ('Первое число больше')
    elif float(a) < float(b):
        print ('Второе число больше')
    else:
        print ('Числа равны')


def numbers (a, b):
    """Checking numbers and final comparing"""
    if len(b) == 0:
        print (info)
        return 1
    elif a.isdigit() and b.isdigit():
        return comparing()
    else:
        try:
            float(a) and float(b)
            return comparing()
        except ValueError:
            print('Ошибка: Вы ввели аргумент, не являющийся числом')
            return 2

print (numbers(a, b))


