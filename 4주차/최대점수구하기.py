def DFS(L,sum):
    global max
    result = 0
    if sum > m:
        for i in range(L - 1):
            result += a[index[i]][0]
        if max < result:
            max = result
    elif sum == m:
        for i in range(L):
            result += a[index[i]][0]
        if max < result:
            max = result

    else:
        for i in range(n):
            if a[i][1] not in res:
                index[L] = i
                res[L] = a[i][1]
                DFS(L+1,sum + a[i][1])
if __name__ == "__main__":
    n, m = map(int,input().split())
    res = [0] * n
    index = [0] * n
    a = []
    max = 0
    for i in range(n):
        a.append(list(map(int,input().split())))
    DFS(0,0)
    print(max)

# n개의 문제를 m이라는 제한 시간안에 풀어야한다. n개의 줄에서 (문제를 맞췄을 때 점수, 푸는데 걸리는 시간)을 입력
# 받고, 제한시간에 받을 수 있은 최대 점수를 구하자. *해당 시간이 지나면 문제를 푼 것으로 간주

# 나의 풀이: 순열처럼 제한 시간을 뽑아서 제한 시간 m을 넘었다면 그 전까지의 즉, L-1 레벨까지 뽑았던 점수를 더한다.
# m과 같다면 L레벨까지 뽑았던 점수를 더한다. => 그 후 점수가 이전의 max 값보다 크면 max를 update 한다.
# 주의해야 할 것은 2차원 배열을 사용하기 때문에 해당 제한시간을 뽑았을 때의 점수를 알아야 하기 때문에 index라는 배열을
# 사용해서 해당 index를 저장했다. L 레벌에서는 i라는 Index를 뽑았고 라는 식으로.
# res 배열에는 뽑았던 문제의 시간제한을 저장하고 이미 앞에서 뽑았던 문제인지 확인을 위함이다. -> if a[][1]not in res[xx]

def dfs(L, sum, time):
    global res
    if time > m:
        return
    if L == n:
        if sum > res:
            res = sum
    else:
        dfs(L+1,sum + score[L],time + pt[L])
        dfs(L+1,sum,time)

if __name__ == "__main__":
    n, m = map(int,input().split())
    score = [] # 점수합을 담을 배열
    pt = [] # 문제 푸는 데 걸리는 시간을 담을 배열
    for i in range(n):
        a, b = map(int,input().split())
        score.append(a)
        pt.append(b)
    res = -2147000000
    dfs(0,0,0)

# 정답풀이: 결국 이 문제에서 포인트는 문제를 풀었냐 안풀었냐이다. 제한 시간안에 얻을 수 있는 최대 점수이기 때문에
# 어떤 문제를 풀었는가에서 점수 합을 구하면 되는 것이다. 이는 부분집합으로 문제를 풀 수 있다.
# {1,2,3,4,5} 1번 ~ 몇 번 문제를 풀었을 때, 시간 제한안이며, 점수가 최대면 된다.
# 시간제한 과 점수 각각 합을 구해야하며 DFS로 문제를 풀기 때문에 매개변수로 전달해가면서 합을 축적해나갈 수 있다.
# 꼭 2차원배열을 활용할 필요는 없다.


# 나는 문제를 풀 때 문제 푸는 순서에 따라서 걸리는 시간이 달라지겠지? 이런 생각을 무심코 순열로 문제를 풀었다... 
