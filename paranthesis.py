
def printParenthesis(str, a): 
    if(a > 0): 
        _printParenthesis(str, 0,  
                          a, 0, 0); 
    return; 
  
def _printParenthesis(str, p, a,  
                      open, close): 
      
    if(close == a): 
        for i in str: 
            print(i, end = ""); 
        print(); 
        return; 
    else: 
        if(open > close): 
            str[p] = '}'; 
            _printParenthesis(str, p + 1, a,  
                              open, close + 1); 
        if(open < a): 
            str[p] = '{'; 
            _printParenthesis(str, p + 1, a,  
                              open + 1, close); 
a = int(input()); 
str = [""] * 2 * a; 
printParenthesis(str, a); 
