# 15664번: N과 M (10)

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [False] * n

result = []


def backTracking(num):
    if len(result) == m:
        print(*result)
        return
    
    remember = 0

    for i in range(num, n):
        if not visited[i] and arr[i] != remember:
            visited[i] = True
            result.append(arr[i])
            remember = arr[i]
            backTracking(i + 1)
            visited[i] = False
            result.pop()


backTracking(0)

