# 임의의 N개 숫자가 입력으로 주어집니다. N개의 수를 오름찾순으로 정렬한 다음 N개의 수중
# 한 개의 수인 M이 주어지면 이분검색으로 M이 정렬된 상태에서 몇 번째에 있는지 구하는 프로그램을 작성하세요

import sys
# sys.stdin = open("in1.txt", "rt")
n, k = map(int, input().split())


list1 = list(map(int, input().split()))

# print(list1)
list1.sort()
# print(list1)



lt = 0
rt = n
while lt <= rt:
    mid = (rt + lt) // 2
    if list1[mid] == k:
        print(mid+1)
        break;
    elif list1[mid] > k:
        rt = mid - 1
    else:
        lt = mid + 1