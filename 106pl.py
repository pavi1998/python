i=int(input())
duplicate =list(map(int,input().strip().split()))[:i]
final_list = [] 
for num in duplicate: 
    if num not in final_list: 
        final_list.append(num) 
for i in final_list:
    print(i,end=" ") 
