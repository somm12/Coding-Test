import sys
input = sys.stdin.readline

def DFS(L):
    global cnt
    if L == m:
        for k in range(m):
            print(res[k], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1,n + 1):
            res[L] = i
            DFS(L+1)
if __name__ == "__main__":
    n, m = map(int,input().split())
    cnt = 0
    res = [0] * m
    DFS(0)
    print(cnt)

# 중복순열이기 때문에 1 ~ n 까지 m개 뽑을 때까지 계속 반복해서 재귀 호출을 해야한다. => for문 n번 반복
# 첫 시작 호출은 루트로 출발하는 것이 항상 확실하다. 여기서는 0을 출발점으로 둔다. => 상태트리의 level 0 부터 시작
# 순열을 출력해야하므로 배열에 순열을 저장하는데, 이 때 계속 경우가 바뀌므로 재할당 방법을 쓰는게 쉽다. => 재귀호출과 세트로 반복

# 즉 level이 0 일때 1,2,3 중 하나를 선택 그 다음 level이 1 일때는 다시 1, 2, 3 중 선택. 이와 같은 방식으로 재귀호출.

