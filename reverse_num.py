m=int(input())
n=list(map(int,input().split()))[0:m]
n.sort(reverse=True)
i=0
while i<m:
    print(n[i],end="\n")
    i+=1
