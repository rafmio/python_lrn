#Определить является ли указанный год високосным
#Год считается високосным, если:
# - кратен 4, но при этом
# - НЕ кратен 100, либо кратен 400
#Вывод: "Обычный", если не високосный, "Високосный", если таковым является

#CheckYear

#X % 4 = 0;
#X %100 != 0;
#X % 400 = 0;

checkyear = int(input())
if checkyear % 4 == 0 and checkyear % 100 != 0 or checkyear % 400 == 0:
    print('Високосный')
else:
    print('Обычный')