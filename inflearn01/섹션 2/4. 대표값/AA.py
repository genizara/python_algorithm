import sys
#sys.stdin = open("in1.txt", "rt")
n = int(input())
a = list(map(int, input().split()))
total = 0
#avg = round(sum(a)/n) # round는 round_half_even 방식을 택함. 즉 round(4.50000) 이면 5가 아니라 4가 됨. 그래서 round 쓰면 안됨
avg = int((sum(a)/n)+0.5) #0.5를 일부러 더함
min=2147000000

for idx, x in enumerate(a):
    tmp = abs(x-avg)
    if tmp < min:
        min = tmp
        score = x
        res = idx+1
    elif tmp == min:
        if x>score:
            score = x
            res = idx+1
