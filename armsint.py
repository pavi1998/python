a,b = list(map(int,input().strip().split()))[:2] 
 
for i in range(a,b+ 1):
   
   sum = 0
 
  
   t = i
   while t> 0 and t!=a and t!=b:
       d = t % 10
       sum += d ** 3
       t//= 10
 
   if i == sum:
       print(i,end=' ')
