u = int(input())
a=[]
for i in range(1,u+1):
  if u%i==0:
     a.append(i)
for n in a:
    print(n,end=" ")   
