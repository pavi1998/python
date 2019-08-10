j,k=map(int,input().split())
m=list(map(int,input().split()))
q=[]
for i in range(0,k):
    a = []
    a=list(map(int,input().split()))
    p = m[a[0]-1]
    for j in range(min(a),max(a)):
        p=p^m[j]
    q.append(p)
for i in range(0,len(q)):
    print(q[i])
