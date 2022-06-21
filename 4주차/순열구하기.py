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

def dfs(L):
    global cnt
    if L == m:
        for j in range(L):
            print(res[j],end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                dfs(L+1)
                ch[i] = 0

if __name__ == "__main__":
    n, m = map(int,input().split())
    res = [0] * n
    ch = [0] * (n + 1)
    cnt = 0
    DFS(0)
    print(cnt)

# 정답풀이: 정답풀이에서는 ch라는 배열을 선언해서 ch[i] = 1와 같이
# 해당 숫자가 순열에 쓰였는지 체크를 한다. 
# 따라서 순열이 m 개가 되었을 때, 순열을 하나 만들었으니 순열을 print하고
# 다시 돌아와서 해당 값을 ch[i] = 0으로 되돌려 줘야한다. 그래야 1 2 ,1 3 하고 다시 2 1 등 만들 수 있다.
 
# 개인적으로는 번거러우니 내가 푼 방법에서 res[:L]를 이용해서 즉 L-1 레발까지 선택한 숫자를 제외한! 수를 선택
# 하는 방식이 편한 것 같다.