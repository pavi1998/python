a=int(input())
c=list(map(int,input().strip().split()))[:a]
while(a>0):
  d=max(c)
  print(d,end="")
  c.remove(d)
  
