#Запросить длины сторон
#Результат вывести по формуле: S = (p(p - a) * (p - b) * (p - c))^2,
#где p = (a + b + c) / 2
a = float(input('Enter a side: '))
b = float(input('Enter b side: '))
c = float(input('Enter c side: '))

p = (a + b + c) / 2

S = float((p(p -a) * (p - b) (p - c)) ** (1 / 2))

print('Square is: ', S)
