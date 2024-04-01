# 15649번: N과 M(1)

n, m = map(int, input().split())

result = []
visited = [False] * (n+1)

def backTracking(num):
    if num == m:
        print(" ".join(map(str, result)))
        return
    
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            backTracking(num + 1)
            visited[i] = False
            result.pop()


def backTracking2(num):
    if num == m:
        print(" ".join(map(str, result)))
        return
    
    for i in range(1, n+1):
        if i not in result:
            result.append(i)
            backTracking2(num + 1)
            result.pop()


# backTracking(0)
backTracking2(0)