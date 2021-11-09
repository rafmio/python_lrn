#request name
#request number of hours and minutes that man sleep daily
#calucate amount of minutes that man sleep daily

name = input('How man''s name? ') 
X = int (input('How many hours does he sleep?'))
print (name, ' sleeps ', X, ' hous a day')
Y = int (input('How many minutes does he sleep daily?'))

sleeptime = X * 60 + Y

print ("Did you know that", name, " sleeps ", sleeptime, ' minutes a day?')
