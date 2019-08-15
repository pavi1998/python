a,f=map(int,input().split())
m,t=map(int,input().split())
k=f-t
r=a-m
if k<0 and r<0:
  print(abs(r),abs(k))
else:  
  print(r,k)
