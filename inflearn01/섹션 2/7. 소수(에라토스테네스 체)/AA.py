import sys
sys.stdin = open("in5.txt", "r")
n = int(input())

#체크리스트
ch = [0] * (n+1)
cnt = 0
for i in range(2, n+1): # n까지 돌아야하니 n+1
    if ch[i] == 0:
        cnt += 1 # 소수의 갯수 셈
        for j in range(i, n+1, i): #세번째는 스텝
            ch[j] = 1


print(cnt)