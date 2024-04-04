# 15663번: N과 M(9)
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

result = []
visited = [False] * n

def backTracking():
    if len(result) == m:
        print(*result)
        return
    remember = 0
    for i in range(n):
        if not visited[i] and remember != arr[i]:
            visited[i] = True
            result.append(arr[i])
            remember = arr[i]
            backTracking()
            visited[i] = False
            result.pop()



backTracking()