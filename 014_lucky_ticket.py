#Счастливый билет
#На входе - шестизначное число
#Счастливый = сумма 3 первых цифр = сумме последних 3 цифр
#Написать программу, которая проверяет счастливый ли билет

tick_ord = 'Обычный'
tick_luck = 'Счастливый'

ticket = input()

tick_part1_1 = int(ticket[0])
tick_part1_2 = int(ticket[1])
tick_part1_3 = int(ticket[2])

tick_part2_1 = int(ticket[3])
tick_part2_2 = int(ticket[4])
tick_part2_3 = int(ticket[5])

sum_part1 = tick_part1_1 + tick_part1_2 + tick_part1_3
sum_part2 = tick_part2_1 + tick_part2_2 + tick_part2_3

if sum_part1 == sum_part2:
    print(tick_luck)
else:
    print(tick_ord)
