#На входе - целые числа
#Если число меньше 10, то пропускаем число
#Если число большее 100, то прекращаем считывать числа
#В остальных случаях вывести число обратно на консоль в
#отдельной строке

x = 0

while True:
    x = int(input())
    if x < 10:
        continue
    elif x > 100:
        break
    else:
        print(x)