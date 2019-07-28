a,b=list(map(int,input().strip().split()))[:2]
for n in range(a,b + 1):
   
    if n > 1 and n!=a and n!=b:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
           print(n,end=' ')
