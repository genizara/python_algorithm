import sys
#sys.stdin = open("in1.txt", "rt")
n, k = map(int, input().split())
a = list(map(int, input().split()))

# 중복을 제거하는 자료구조 : set
res = set()
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i] + a[j] + a[m])

# set 에는 sort 기능이 없음
res=list(res)
res.sort(reverse=True) # 내림차준 정렬
print(res[k-1])
