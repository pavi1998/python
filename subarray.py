def lm(ar, k) : 
	p = 1
	l = 1
	for o in range(1, k) : 
		if (ar[o] > ar[o-1]) : 
			l =l + 1
		else :
			if (p < l) : 
				p = l 
			l = 1
	if (p < l) : 
		p = l 
	return p 

n =int(input()) 
arr =list(map(int,input().split()))
print(lm(arr, n)) 
