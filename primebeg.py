mun = int(input())
if mun > 1:
    for i in range(2, mun):
        if (mun % i) == 0:
            print(" no")
            break
    else:
        print(" yes")
