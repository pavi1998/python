e,b=map(int,input().split())
c=list(map(int,input().strip().split()))[:e]
a=[]
a.append(c)
m1=a[0]
m2=a[1]
if a[1]<=a[0]:
   max1=a[1]
   max2=a[0]
for num in a:
  if num>=max1 and num<max2:
    max1=num
  elif num>=max2:
    max1=max2
    max2=num
  else:
    pass
print(max1)          
