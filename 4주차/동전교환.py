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