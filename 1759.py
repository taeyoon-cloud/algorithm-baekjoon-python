# 1759번: 암호 만들기

l, c = map(int, input().split())
arr = sorted(list(input().split()))

vowels = ['a', 'e', 'i', 'o', 'u'] # 모음
result = []
visited = [False] * c

def is_possible(arr):
    vowels_cnt = 0
    consonant_cnt = 0
    for c in arr:
        if c in vowels:
            vowels_cnt += 1
        else:
            consonant_cnt += 1
    if vowels_cnt > 0 and consonant_cnt > 1:
        return True
    else:
        return False

def backTracking(num):
    if len(result) == l and is_possible(result):
        print("".join(result))
        return
    
    for i in range(num, c):
        if not visited[i]:
            result.append(arr[i])
            visited[i] = True
            backTracking(i + 1)
            result.pop()
            visited[i] = False



backTracking(0)
