def decimalToBinary(n):
    
    if n > 1:
        decimalToBinary(n // 2)
    print(n % 2, end='')


# decimal number
number = int(input())

decimalToBinary(number)
