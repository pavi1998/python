b=int(input())
for i in range(1, b+1):
    if b % i == 0:
        if i % 2 != 0:
            print(i,end=" ")
