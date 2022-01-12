import sys
#sys.stdin = open("in1.txt", "rt")
n = int(input())
a = list(map(str, input().split()))

def digit_sum(x):
    res = 0
    for j in range(len(x)):
        res += int(x[j])
    return res

max = 0
res = ""
for k in a:
    tmp = digit_sum(k)
    if max < tmp:
        max = tmp
        res = k

print(res)








