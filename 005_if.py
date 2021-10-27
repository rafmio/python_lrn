a = int(input('Введите значение a: '))
b = int (input('Введите значение b: '))

if b != 0:
    print (a / b)
else:
    print('Деление на 0 невозможно')
    b = int(input('Введите ненулевое значение b: '))
