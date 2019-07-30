n=int(input())
a=1
b=1
count=0
while(count<n):
    print(a,end=' ')
    c=a+b
    a=b
    b=c
    count+=1
