n = int(input())
arr=list(map(int,input().strip().split()))[:n]
for i in arr:
  c=n|i
print(c) 
