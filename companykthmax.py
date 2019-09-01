k,h=map(int,input().split())
c=list(map(int,input().strip().split()))[:k]
for i in range(0,h-1):
    c.remove(max(c))
    print(max(c))
