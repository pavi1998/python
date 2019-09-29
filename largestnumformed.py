c=int(input())
d=list(map(int,input().split()))[:c]
for i in range(0,c):
  m=max(d)
  print(m,end="")
  d.remove(max(d))

