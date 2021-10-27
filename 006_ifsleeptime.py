#Рекомендованное время сна, минимум: значение A
A = int(input('Enter minimal sleeptime: '))
#Рекомандованное время сна, максимум: значение B
B = int(input('Enter maximal sleeptime: '))
#Текущее количество часов сна: значение H
H = int(input('Enter current sleeptime value: '))
#Если текущее время менее рекомендованного - ввести "Недосып"
#Если текущее время более максимального - вывести "Пересып"
if A <= H <= B:
    print("Это нормально")
elif H < A:
    print("Недосып")
else:
    print("Пересып")

