def printSubsets(n): 
      
    for i in arr: 
          
        c=n&i 
    print(i, end = "") 
  
# Driver code 
n = int(input())
arr=list(map(int,input().strip().split()))[:n]
printSubsets(n) 
