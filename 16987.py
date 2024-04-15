# 16987번: 계란으로 계란치기
import sys
input = sys.stdin.readline

n = int(input()) # 계란 개수
eggs = []
for _ in range(n):
    durability, weight = map(int, input().split())
    eggs.append([durability, weight])

answer = -1

def check(eggs):
    temp = 0
    for egg in eggs:
        if egg[0] <= 0:
            temp += 1
    return temp

# num = 현재 손에 든 계란의 인덱스
def backTracking(num):
    global answer

    if num == n:
        answer = max(answer, check(eggs))
        return

    if eggs[num][0] <= 0: # 현재 손에 쥔 계란이 깨졌다면 다음 계란으로 넘어간다.
        backTracking(num+1)
    else: # 현재 손에 쥔 계란이 깨지지 않았다면 다른 계란과 부딪혀본다.
        is_all_broken = True
        for i in range(n):
            if num != i and eggs[i][0] > 0:
                is_all_broken = False
                eggs[i][0] -= eggs[num][1]
                eggs[num][0] -= eggs[i][1]
                backTracking(num+1)
                eggs[i][0] += eggs[num][1]
                eggs[num][0] += eggs[i][1]
        if is_all_broken: # 계란이 모두 깨진 경우에는 바로 재귀함수 탈출
            backTracking(n)
    



backTracking(0)
print(answer)