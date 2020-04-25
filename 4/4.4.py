def MinDivisor(n):
    import math
    i = 2
    while n % i != 0:
        if i >= math.sqrt(n):
            print(n)
            return
        i += 1
    print(i)
n = int(input())
MinDivisor(n)
