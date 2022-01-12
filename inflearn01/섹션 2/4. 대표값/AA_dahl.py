import sys
#sys.stdin = open("in1.txt", "rt")
n = int(input())
a = list(map(int, input().split()))
total = 0
for k in range(n):
    total += a[k]

avg = total/n
rAvg = round(avg)

minAbs = 99999
res = -1
for k in range(n):
    abs1 = abs(a[k] - rAvg)
    if minAbs > abs1:
        minAbs = abs1
        res = k

print("%d %d" %(rAvg, res+1))


