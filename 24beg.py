n=int(input())
c=list(map(int,input().strip().split()))[:n]
u=sorted(c)
for i in u:
  print(i,end=" ")
