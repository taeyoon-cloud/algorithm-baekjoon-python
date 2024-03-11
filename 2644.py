# 2644번: 촌수 계산
from collections import deque

import sys
sys.setrecursionlimit(10**9)

n = int(input()) # 사람 수
a, b = map(int, input().split()) # 촌수를 계산해야 하는 사람 번호
m = int(input()) # 부모 자식 간 관계 개수

graph = [[] for _ in range(n + 1)] # 인덱스에 해당하는 자식 번호를 저장하는 리스트

for _ in range(m):
    x, y = map(int, input().split()) # x는 y의 부모
    # 그냥 bfs를 돌면서 a - b 사이 경로의 개수를 세면 되므로, 방향은 중요하지 않다.
    # 그러므로 둘 다 추가
    graph[x].append(y)
    graph[y].append(x)

distance = [-1] * (n+1) # 거리를 저장하는 리스트 (-1이면 방문x)

# # 임의로 a에서 시작해서 b까지의 촌수를 확인하다고 하자.
# q = deque([a])
# distance[a] = 0

# while q:
#     now = q.popleft()
#     dist = distance[now]

#     for i in graph[now]:
#         if distance[i] < 0:
#             distance[i] = dist + 1
#             q.append(i)

# # a -> b까지의 거리 출력
# print(distance[b])
    


distance[a] = 0

def dfs(now):
    for i in graph[now]:
        if distance[i] < 0:
            distance[i] = distance[now] + 1
            dfs(i)

dfs(a)
print(distance[b])


