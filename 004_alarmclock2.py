#Кате для сна нужно X минут
X = int(input())
  
#Катя ложится спать в H часов:
H = int(input())
  
#...и M минут:
M = int(input())
  
#Вывести время, на которое нужно поставить будильник, чтобы проспать X минут
#Вывод часов и минут - на разные строки
  
minaftmidn = H * 60 + M
alarmclock = minaftmidn + X
Halarm = alarmclock // 60
Malarm = alarmclock % 60
  
print (Halarm)
print (Malarm)
