j,o=list(map(int,input().strip().split()))[:2]
j,o= (j^o)^((j^o)^o),(j^o)^o
print(j,o)
