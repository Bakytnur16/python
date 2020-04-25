def IsPrime(n):
    k = 2
    while n % k != 0:
        if k >= n**0.5:
            return True
        k += 1
    return False
n = int(input())
if IsPrime(n) or n == 2:
    print('YES')
else:
    print('NO')
