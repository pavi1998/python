m,g = list(map(int,input().strip().split()))[:2] 
i=1
while(i <= m and i <= g):
    if(m % i == 0 and g % i == 0):
        gcd = i
    i = i + 1
print(gcd)       
