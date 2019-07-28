a,b, = list(map(int,input().strip().split()))[:2] 
for i in range(a,b+1):
    if i%2==0:
        print(i,end=' ')
