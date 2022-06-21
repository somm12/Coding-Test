def DFS(L):
    global res, min
    if sum(res) > M:
        return
    count = 0
    for k in res:
        if k != 0:
            count += 1
    if min < count:
        return
    if sum(res) == M:
        if min > count:
            min = count
        return

    else:
        for i in range(n):
            res[L] = coins[i]
            DFS(L+1)

if __name__ == "__main__":
    n = int(input())
    coins = list(map(int,input().split()))
    coins.sort(reverse=True)
    M = int(input())
    res = [0] * M
    min = 21470000
    DFS(0)
    print(min)
# 거스름돈 종류 n개를 가지고 m원 거슬러 줘야한다. 동전은 무한히 사용할 수 있으며 최소한의 
# 동전 개수로 거슬러 준다면 몇 개의 동전이 필요한지?
# 나의 풀이: 중복순열을 DFS재귀로 호출 한 것과 비슷한 문제로, 일단 최소한의 개수를 구하기 위해
# 입력 받은 동전종류 배열을 내림차순으로 정렬한다. 가장 큰 동전이 먼저 더해져서 최소한의 개수에 도달가능.
# res배열에 각 레벨에서 선택한 숫자를 담고 sum을 해서 m과 같은지 확인, 또한 개수가 최소인지 현재의 min(최소 동전개수)가
# res의 원소 중 0이 아닌것들 보다 큰 지 확인.


def dfs(L,sum):
   global min
   if L > min:
       return
   if sum > M:
       return
   if sum == M:
       if L < min:
           min = L
   else:
        for i in range(n):
            dfs(L+1, sum + a[i])
if __name__ == "__main__":
    n = int(input())
    a = list(map(int,input().split()))
    m = int(input())
    min = 21470000
    a.sort(reverse=True)
    DFS(0,0)
    print(min)
    
# 정답풀이 : 내 풀이에서 아쉬운 것은 
# 1. 합과 그 개수를 구하는 것이기 때문에 합은 DFS 매개변수로 sum을 전달하면서
# DFS(L+1,sum + coins[i]) 으로 재귀 호출을 하면 그 경우의 sum이 계속 유지되기 때문에 굳이 res배열을 쓸 필요 없다는것
# 2. 트리를 그려보면 각 레벨이 곧 동전을 고른 개수와 같기 때문에 min = L 과 같이 사용할 수 있다.
# 따라서 굳이 for문 으로 res 배열에서 0 이 아닌 수를 count해서
# 최소인지 확인하는 방법으로 쓰지 않아도 된다.
# ****** 하지만 정답 방법으로 문제를 풀 경우, 시간초과를 방지하기 위해 if L > min 면 return 추가한다.
# 현재의 min 개수가 최소개수 후보인데, 재귀호출을 계속하면서 L이 커지고 합을 m 구해도 의미가 없다.