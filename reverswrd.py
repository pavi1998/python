def reverseWordSentence(a):  
    w= a.split(" ") 
    m = [s[::-1] for s in w] 
    p = " ".join(m) 
    return p  
a = input() 
print(reverseWordSentence(a)) 
