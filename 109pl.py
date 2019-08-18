from itertools import accumulate 
  
def cumulativeSum(input): 
      c=list(accumulate(input))
      for i in reversed(c):
        print(i,end=" ")
     
  
# Driver program 
if __name__ == "__main__": 
    o=int(input())
    input=list(map(int,input().strip().split()))[:o] 
    cumulativeSum(input) 
