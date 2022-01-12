import sys
sys.stdin = open("in1.txt", "rt")
T = int(input())
for t in range(T):
    n,s,e,k = map(int, input().split())
    a = list(map(int, input().split()))

    a = a[s-1:e]    # slice 를 사용. s-1을 해야 s번째가 됨
    a.sort()        # 오름차준 정렬
    print("#%d %d" %(t+1, a[k-1]))   # k번째를 보려면 k-1



