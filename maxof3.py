a,b,c = list(map(int,input().strip().split()))[:3] 
if a>b and a>c:
  print(a)
elif b>c:
  print(b)
else:
  print(c)