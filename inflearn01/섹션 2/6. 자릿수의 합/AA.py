import sys
sys.stdin = open("in5.txt", "rt")
n = int(input())
a = list(map(int, input().split()))

def digit_sum(x):
    sum=0
    while x > 0:
        sum += x % 10
        x = x//10
    return sum

max = 0
res = ""
for k in a:
    tmp = digit_sum(k)
    if max < tmp:
        max = tmp
        res = k

print(res)