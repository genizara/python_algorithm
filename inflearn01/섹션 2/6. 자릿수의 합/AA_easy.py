import sys
sys.stdin = open("in1.txt", "rt")
n = int(input())
a = list(map(str, input().split()))

def digit_sum(x):
    sum=0
    for i in str(x):
        sum += int(i)
    return sum

max = 0
res = ""
for k in a:
    tmp = digit_sum(k)
    if max < tmp:
        max = tmp
        res = k

print(res)