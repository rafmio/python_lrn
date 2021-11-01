#На входе запросить тип фигуры:
#     - треугольник
#     - прямоугольник
#     - круг
#Число Пи = 3.14
#Формула площади круга: S = пR ^2
#Формула площади треугольника: S = float(    (p * (p - a) * (p - b) * (p - c)) ** (1/2)    )
#     где p = (a + b + c) / 2

figure = input()

if figure == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = None
    p = (a + b + c) / 2
    St = float(  (p *(p - a) * (p - b) * (p - c)) ** (1/2) )    #S triangle formula

    print (St)
    
elif figure == 'прямоугольник':
    a = int(input())
    b = int(input())
    Sre = float(a * b)    #S rectangle formula
    print(Sre)
  
elif figure == 'круг':
    Cr = int(input())     #Circle radius
    Pi  = float(3.14)
    Sci = float (Pi * Cr ** 2) #S circle forlula
    print(Sci)
    
else:
    print('Unknown fugure')
