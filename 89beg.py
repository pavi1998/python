def lexicographi_sort(s):
    return sorted(sorted(s), key=str.upper)
m=input()
c=lexicographi_sort(m)
for i in c:
  print(i,end="")
