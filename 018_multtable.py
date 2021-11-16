#На входе принять 4 значения - целые числа
#Вывести фрагмент таблицы умножения отрезка [a;b] на отрезок [c;d]
#Вводимые числа менее 10б a <= b, c <= d
a = int(input())
b = int(input())
c = int(input())
d = int(input())


for ii in range(c, d + 1):
    print('\t', ii, end='')
print()

for i in range(a, b + 1):
    print(i, end='\t')
    for j in range(c, d + 1):
        print(i * j, end='\t')
    print()