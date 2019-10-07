n=int(input())
sum=0
fact=1
while(n>0):
  p=n%10
  sum=sum+p
  n=n//10
  fact=fact*p
  c=sum
g=c+fact
if g==n:
  print("Great")
else:
  print(g)  
