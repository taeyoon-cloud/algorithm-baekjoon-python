# 1926번: 그림(BFS)
import sys
from collections import deque
input = sys.stdin.readline

cnt = 0 # 그림 개수
max_area = 0 # 가장 넓은 그림의 넓이

n, m = map(int, input().split())
visited = [[False] * m for _ in range(n)]
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    global max_area
    q = deque([(x, y)])
    visited[x][y] = True
    area = 1

    while q:
        now = q.popleft()
        now_x = now[0]
        now_y = now[1]

        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if not visited[nx][ny] and arr[nx][ny] == 1:
                    q.append([nx, ny])
                    visited[nx][ny] = True
                    area += 1
    
    max_area = max(area, max_area)



for i in range(n):
    for j in range(m):
        if not visited[i][j] and arr[i][j] == 1:
            bfs(i, j)
            cnt += 1

print(cnt)
print(max_area)