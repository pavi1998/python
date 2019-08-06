    
def pavi(l):
    n="abcdefghijklmnopqrstuvwxyz"
    for m in n:
        if m not in l.lower():
            return False
    return True
lo=input()
if (pavi(lo)==True):
    print("yes")
else:
    print("no")
