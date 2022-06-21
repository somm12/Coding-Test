def DFS(L):
    global cnt, res
    if L == m:
        for i in res:
            print(i, end= ' ')
        print()
        cnt += 1
    else:
        for i in range(1,n+1):
            if i not in res[:L]:
                res[L] = i
                DFS(L+1)

if __name__ == "__main__":
    n, m = map(int,input().split())
    res = [0] * m
    cnt = 0
    DFS(0)
    print(cnt)

# 중복순열 구하기에서 중복만 뺀 것으로, 앞에서 선택한 수는 포함하지 않아야한다.
# 나의 풀이: L 즉, 현재 레벨 전까지 선택한 수들은 제외하고 선택해야하므로, res[:L] 배열에 속하지 않은 
# 수를 선택해서 순열을 만들어 나가는 방식으로 구현했다.

