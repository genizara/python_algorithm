# 임의의 N개 숫자가 입력으로 주어집니다. N개의 수를 오름찾순으로 정렬한 다음 N개의 수중
# 한 개의 수인 M이 주어지면 이분검색으로 M이 정렬된 상태에서 몇 번째에 있는지 구하는 프로그램을 작성하세요

import sys
sys.stdin = open("in2.txt", "rt")
n, k = map(int, input().split())


list1 = list(map(int, input().split()))

smaller = 0
for i in list1:
    if k > i :
        smaller += 1

print(smaller + 1)

