#Запросить три строки
#   первое вещественное число
#   второе вещественное число
#   операция
""""
Поддерживаемые операции: +, -, /, *, mod, pow, div, где
mod — это взятие остатка от деления,
pow — возведение в степень,
div — целочисленное деление.

Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

Обратите внимание, что на вход программе приходят вещественные числа.
"""
x = float(input())
y = float(input())
operation = input()

if y == 0 and operation == 'div':
    print('Деление на 0!')
elif y == 0 and operation == 'mod':
    print('Деление на 0!')
elif y == 0 and operation == '/':
    print('Деление на 0!')
elif operation == '+':
  print(x + y)
elif operation == '-':
  print(x - y)
elif operation == '/':
  print(x / y)
elif operation == '*':
  print (x * y)
elif operation == 'mod':
  print(x % y)
elif operation == 'pow':
  print(x ** y)
elif operation == 'div':
  print(x // y)
