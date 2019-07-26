p = int(input())
sum = 0
temp = p
while temp > 0:
   r = temp % 10
   sum += r ** 3
   temp //= 10
if p == sum:
   print("yes")
else:
   print("no")
