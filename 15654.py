# 15654번: N과 M(5)

n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort() # arr리스트 정렬
visited = [False] * len(arr)
result = []


def backTracking(num):
    if num == m:
        print(*result)
        return
    
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            result.append(arr[i])
            backTracking(num + 1)
            result.pop()
            visited[i] = False

# backTracking(0)
    


def backTracking2(num):
    if num == m:
        print(*result)
        return
    
    for i in range(n):
        if arr[i] not in result:
            result.append(arr[i])
            backTracking2(num + 1)
            result.pop()

backTracking2(0)
