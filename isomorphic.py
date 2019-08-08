m,n = map(str,input().split())
x = {}; y = {}
def is_isomorphic(m,n):
    if len(m) != len(n):
        return False
    else:
        for i, v in enumerate(m):
            if v in x and x[v] != n[i]:
                return False
            else:
                x[v] = n[i]
            if n[i] in y and y[n[i]] != v:
                return False
            else:
                y[n[i]] = v
        return True
z=is_isomorphic(m,n)
if (True==z):
  print("yes")
else:
  print("no")
