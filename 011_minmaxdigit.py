#Request promt 3 amounts
#Output in text order:
#       1.Max value
#       2.Min value
#       3.Remainted value
#Values may be the same

a = int(input())
b = int(input())
c = int(input())

if b <= a >= c:
      maxval = a
      if b >= c:
          minval = c
          othval = b
      elif b < c:
          minval = b
          othval = c
          
if a <= b >= c:
      maxval = b
      if a >= c:
          minval = c
          othval = a
      elif a < c:
          minval = a
          othval = c
          
if b <= c >= a:
      maxval = c
      if b >= a:
          minval = a
          othval = b
      elif b < a:
          minval = b
          othval = a


print(maxval)
print(minval)
print(othval)

