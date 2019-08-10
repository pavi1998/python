def firstDigit(q) : 
  
    
    while q >= 10:  
        q = q / 10; 
      
    
    return int(q) 
  
# Find the last digit 
def lastDigit(q) : 
  
    # return the last digit 
    return (q % 10) 
  
# Driver Code 
q = int(input()) 
print(firstDigit(q)+lastDigit(q), end = " ")  

