# 15650번: N과 M(2)


n, m = map(int, input().split())

result = []
visted = [False] * (n+1)
def backTracking(x):
    if len(result) == m:
        print(" ".join(map(str, result)))
        return

    for i in range(x+1, n+1):
        if i not in result:
            result.append(i)
            backTracking(i)
            result.pop()

backTracking(0)