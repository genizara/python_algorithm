# 창고 정리
# 창고에 상자가 가로방향으로 일렬로 쌓여 있습니다.
# 만약 가로의 길이가 7이라면
# 1열은 높이가 6으로 6개의 상자가 쌓여 있고, 2열은 3개의 상자, 3열은 9개의 상자가 쌓여 있
# 으며 높이는 9라고 읽는다.
# 창고 높이 조정은 가장 높은 곳에 상자를 가장 낮은 곳으로 이동하는 것을 말한다.
# 가장 높은 곳이나 가장 낮은 곳이 여러곳이면 그 중 아무거나 선택하면 된다.
# 위에 그림을 1회 높이 조정을 하면 다음과 같아진다.
# 1
# 1
# 창고의 가로 길이와 각 열의 상자 높이가 주어집니다. m회의 높이 조정을 한 후 가장 높은 곳
# 과 가장 낮은 곳의 차이를 출력하는 프로그램을 작성하세요.
# 침몰하는 타이타닉(그리디)
# 유럽에서 가장 유명했던 유람선 타이타닉이 침몰하고 있습니다. 유람선에는 N명의 승객이 타고
# 있습니다. 구명보트를 타고 탈출해야 하는데 타이타닉에 있는 구명보트는 2명 이하로만 탈 수 있
# 으며, 보트 한 개에 탈 수 있는 총 무게도 M kg 이하로 제한되어 있습니다.
# N명의 승객 몸무게가 주어졌을 때 승객 모두가 탈출하기 위한 구명보트의 최소개수를 출력하는
# 프로그램을 작성하세요.
# ▣ 입력설명
# 첫째 줄에 자연수 N(5<=N<=1000)과 M(70<=M<=250)이 주어집니다.
# 두 번째 줄에 N개로 구성된 몸무게 수열이 주어집니다. 몸무게는 50이상 150이하입니다.
# 각 승객의 몸무게는 M을 넘지는 않습니다. 즉 탈출을 못하는 경우는 없습니다.
# ▣ 출력설명
# 첫째 줄에 구명보트의 최소 개수를 출력합니다.
# ▣ 입력예제 1
# 5 140
# 90 50 70 100 60
# ▣ 출력예제 1
# 3


import sys

def onboard(leftWeight, n, onboardWei):
    totalOnboard = 0
    if len(onboardWei) < 2:
        for i in range(n):
            if leftWeight >= list1[i]:
                heaviest = list1.pop(i)
                leftWeight -= heaviest
                onboardWei.append(heaviest)
                n -= 1
                totalOnboard += 1
                totalOnboard += onboard(leftWeight, n, onboardWei)
                break

    return totalOnboard


# sys.stdin = open("in4.txt", "rt")
n, m = map(int, input().split())
list1 = list(map(int, input().split()))

# print(n)
# print(m)
# print(list1)

list1.sort(reverse=True)
totalBoatNeed = 0
# print(list1)
while n > 0:
    onboardWei = []
    n -= onboard(m, n, onboardWei)

    totalBoatNeed += 1
    # print(totalBoatNeed, " ", onboardWei)

print(totalBoatNeed)