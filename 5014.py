# 5014번: 스타트링크
from collections import deque
import sys
input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())

building = [-1] * (f+2) # 건물의 층 수(방문하지 않은 경우 -1)
building[s] = 0 # 시작점까지 누른 버튼의 수는 0

q = deque([s]) # 방문한 층을 저장하는 큐, 시작층을 넣고 시작

# BFS 시작
while q:
    now = q.popleft()

    for i in [u, -d]:
        new_now = now + i

        if new_now > 0 and new_now <= f:
            if building[new_now] == -1:
                building[new_now] = building[now] + 1
                q.append(new_now)

    if building[g] != -1:
        break


if building[g] == -1:
    print("use the stairs")
else:
    print(building[g])

