# 1946번: 신입 사원
import sys
input = sys.stdin.readline
t = int(input()) # 테스트 케이스 수


while t:
    n = int(input()) # 지원자 숫자
    score = []
    for _ in range(n):
        each_score = list(map(int, input().split()))
        score.append(each_score)

    score.sort() # 서류 심사 성적 기준으로 오름차순 정렬
    
    cmp_rank = score[0][1] # 처음에 뽑는 면접 성적 순위
    cnt = 1 # 선발할 수 있는 신입 사원 수
    for i in range(1, n):
        if cmp_rank > score[i][1]: # 현재 확인하는 사람의 면접 성적 순위가 더 작은 경우에만 선발할 수 있다.
            cmp_rank = score[i][1] # 현재 선발한 사람의 면접 성적 순위로 비교 기준이 될 면접 성적 순위를 갱신한다.
            cnt += 1
    
    print(cnt)
    t -= 1