a = []
def DFS(n):
    if n > 3:
        for i in a:
            print(i, end=' ')
        print() 
        return
    else:
       a.append(n)
       DFS(n+1)
       a.pop()
       DFS(n+1)
# ------^나의 풀이
def dfs(v):
    if v == n + 1:
        for i in range(1, n + 1):
            if ch[i] == 1:
                print(i, end= ' ')
        print()
    else:
        ch[v] = 1
        dfs(v + 1)
        ch[v] = 0
        dfs(v + 1)

if __name__ == "__main__":
    n = int(input())
    ch = [0] * (n + 1)
    dfs(1)
# ------^정답 풀이

# 원소가 1 2 3인 집합의 부분집합 구하기.
# 나의 풀이 : append와 pop을 이용해서 문제를 풀었음. DFS를 이용한 부분집합은 재귀를 이용해서 왼쪽 노드
# 방향으로는 해당 원소를 포함, 오른쪽 방향으로는 해당원소를 포함하는 않는 방향으로 반복적으로 호출, 제일 큰
# 원소의 수보다 커질 때가 종료시점.

# 정답 풀이: 배열에 원소를 0 과 1을 할당해서 1일 때는 포함하고 0일 때는 포함하지 않는다는 뜻으로 배열을 
# 이용한다.