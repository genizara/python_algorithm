import sys
#sys.stdin = open("in1.txt", "rt")
n, m = map(int, input().split())


arr = [0] * (n+m+1)

for i in range(n):
    for j in range(m):
        arr[i + 1 + j + 1] += 1

max = 0

for k in arr:
    if k > max:
        max = k


for k in range(n+m+1):
    if max == arr[k]:
        print(k, end=' ')

