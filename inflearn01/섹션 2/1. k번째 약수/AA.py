import sys
sys.stdin=open("in5.txt", "rt")
n, k=map(int, input().split())
cnt=0
print(k)
print(n)
for i in range(1, n+1):
    if n%i==0:
        cnt+=1
    if cnt==k:
        print(i)
        break
else: # 21.11.06 이런 문법이 된다고?
    print(-1)

