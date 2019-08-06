def commonPrefixUtil(s1, s2): 

	result = ""; 
	n11 = len(s1) 
	n22 = len(s2) 
	a = 0
	b = 0
	while a <= n11 - 1 and b <= n22 - 1: 
	
		if (s1[a] != s2[b]): 
			break
			
		result += s1[a] 
		a += 1
		b += 1

	return (result) 

def commonPrefix (arr, n): 

	prefix = arr[0] 

	for a in range (1, n): 
		prefix = commonPrefixUtil(prefix, arr[a]) 

	return (prefix) 


n=int(input())
arr =[]
for a in range(0,n):
  l = input()
  arr.append(l)
ans = commonPrefix(arr, n) 

if (len(ans)): 
	print (ans);
