def printRepeating(arr, size): 
  
    
    for i in range (0, size): 
        for j in range (i + 1, size): 
            if arr[i] == arr[j]: 
                print(arr[i], end = ' ') 
            else:
            print("unique")                  
      
# Driver code 
m=int(input())
arr =list(map(int,input().strip().split()))[:m]
arr_size = len(arr) 
printRepeating(arr, arr_size) 
  
