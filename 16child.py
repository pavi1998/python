p=int(input())
r=list(map(int,input().split()))
c=[1]*p
for i in range(p):
    if(i==0):
        if r[i]>r[i+1]:
            c[i]+=c[i+1]
    else:
        if r[i]>r[i-1]:
            c[i]+=c[i-1]
print(sum(c))
