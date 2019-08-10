m,n=map(int,input().split())
u=list(map(int,input().split()))[:m]
if n in u:
  print(n)
else:
  print(n-1)  
