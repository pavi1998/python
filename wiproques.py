c=int(input())
sum=0
while(c>0):
    r=c%10
    if(r%2!=0):
      sum=sum+r
    else:
      d=r
    c=c//10
print(sum)

       
