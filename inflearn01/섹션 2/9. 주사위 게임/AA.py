import sys
#sys.stdin = open("in5.txt", "rt")

n = int(input())
res = 0
for i in range(n):
    tmp = input().split()
    tmp.sort() # 오름차순 정렬
    a,b,c = map(int, tmp)

    if a==b and b==c :
        money = 10000 + a * 1000
    elif a==b or a==c : #계산시 한 눈으로 잡아서 하기위해
        money = 1000 + ( a * 100 )
    elif b==c :
        money = 1000 + ( b* 100 )
    else:
        money = 100 * c # c가 제일 큰 값임

    if money > res:
        res = money

print(res)