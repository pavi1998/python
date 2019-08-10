

def areParanthesisBalanced(ex) :  
  
    s = [];  
  
    
    for i in range(len(ex)) : 
  
        if (ex[i] == '(' or 
            ex[i] == '[' or ex[i] == '{') : 
  
            # Push the element in the stack  
            s.append(ex[i]);  
            continue;  
  
        # IF current character is not opening  
        # bracket, then it must be closing.   
        # So stack cannot be empty at this point.  
        if (len(s) == 0) : 
            return False;  
  
        if ex[i] == ')' : 
  
            # Store the top element in a  
            x = s.pop(); 
              
            if (x == '{' or x == '[') : 
                return False;  
  
        elif ex[i] == '}':  
  
            # Store the top element in b  
            x = s.pop(); 
              
            if (x == '(' or x == '[') : 
                return False;  
          
        elif x == ']':  
  
            # Store the top element in c  
            x = s.pop(); 
              
            if (x =='(' or x == '{') : 
                return False;  
  
    # Check Empty Stack  
    if len(s) : 
        return True
    else : 
        return False
  
# Driver Code 
if __name__ == "__main__" :  
  
    ex = input();  
  
    if (areParanthesisBalanced(ex)) : 
        print("no");  
    else : 
        print("yes"); 
