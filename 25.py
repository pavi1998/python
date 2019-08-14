n=int(input())
c=list(map(int,input().strip().split()))[:n]
u=sorted(c)
m=len(u)//2
print(u[m])
