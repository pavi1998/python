m=int(input())
s=0
while(m>0):
  u=m%10
  s=s+u*u
  m=m//10
print(s)
