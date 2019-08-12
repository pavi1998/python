def catalan(n): 
    if n <=1 : 
        return 1 
   
    res = 0 
    for i in range(n): 
        res += catalan(i) * catalan(n-i-1) 
  
    return res 
p=int(input())
for i in range(p+1): 
    print(catalan(i),end=" ") 
