j,k=map(int,input().split())
t=(input().split())[0:j] 
i=0
while i<k:
  m,h=map(int,input().split())
  i+=1
  print(min(t[m-1:h])) 
