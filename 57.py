j,k=map(int,input().split())
l=list(map(int,input().strip().split()))[:j]
if k in l:
  c=l.count(k)
  print(c)  
