#Запросить число x
#Вывести True, если
#   -15 < x <= 2 or 15 < x < 17 or x >= 19
#В противном случае вывести False
x = int(input())
if (-15 < x <= 12) or (14 < x < 17) or (x >= 19):
    print('True')
else:
    print('False')
