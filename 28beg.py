n=int(input())
c=list(map(int,input().strip().split()))[:n]
u=sorted(c)
for i in (0,n+1):
   print(i,u[i])
  
