import sys
#sys.stdin = open("in5.txt", "r")

# 뒤집는 함수
def reverse(x):
    res = 0
    while x > 0:
        t = x % 10
        res = res * 10 + t
        x = x // 10

    return res

# 소수인지 판별하는 함수
def isPrime(x):
    if x == 1:
        return False

    for i in range(2, x//2 + 1) : # 절반 까지만 돔.
        if x % i == 0:
            return False
    else : # for - else 구문!?!?!?!?
        return True


n = int(input())
a = list(map(int, input().split()))

#
for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')
