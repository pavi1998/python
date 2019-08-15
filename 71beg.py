def reverse(s): 
    return s[::-1] 
  
def isPalindrome(s): 
    rev = reverse(s)  
    if (s == rev): 
        return True
    return False

s =str(input())
a = isPalindrome(s) 
  
if a == 1: 
    print("Yes") 
else: 
    print("No") 
