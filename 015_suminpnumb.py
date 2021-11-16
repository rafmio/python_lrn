#Запрашивать целые числа
#Запрашивать до тех пор, пока введенное значение не окажется нулем
sum1 = 0
inpval = None 

while inpval != 0:
    inpval = int(input())
    sum1 += inpval

print(sum1)
