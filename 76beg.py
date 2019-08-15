u = int(input())
if u> 1:
    for i in range(2, u):
        if (u % i) == 0:
            print("yes")
            break
    else:
        print("no")
