num1,num2=map(int,input().split())
lcm = num1 if(num1 > num2) else num2
while(True):
    if((lcm % num1 == 0) and (lcm % num2 == 0)):
        print(lcm)
        break
    lcm += 1
