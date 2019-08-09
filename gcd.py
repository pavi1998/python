v,e = list(map(int,input().strip().split()))[:2] 
i=1
while(i <= v and i <= e):
    if(v % i == 0 and e % i == 0):
        gcd = i
    i = i + 1
print(gcd)       
