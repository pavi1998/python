a=int(input())
sum=0
while(a>0):
  u=a%10
  sum=sum+u*u
  a=a//10
print(sum)
