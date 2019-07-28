m,n, = list(map(int,input().strip().split()))[:2] 
for i in range(m,n+1):
      order = len(str(i))
      sum = 0
      temp = i      
while temp > 0:
       digit=temp % 10
       sum +=digit ** order
       temp //= 10
if i== sum:
       print(i)

