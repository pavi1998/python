pp=int(input())
a=list(map(int,input().split()))[:pp]
c=0
for i in range(pp):
    c+=a[i]
d=c//pp
print(d)
