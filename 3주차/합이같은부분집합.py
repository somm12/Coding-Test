def DFS(index):
    if index == len(arr):
        add = 0
        removeSet = []
        for i in range(1,arr[n - 1] + 1):
            if ch[i] == 1:
                add += i
                removeSet.append(i)
        removeSet = set(removeSet)
        if sum(set(arr) - removeSet) == add:
            result.append("YES")
        #  진행 중이던 모든 재귀종료는 할 수 있나?

    else:
        ch[arr[index]] = 1
        DFS(index + 1)
        ch[arr[index]] = 0
        DFS(index + 1)


if __name__ == "__main__":
    result = []
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    ch = [0] * (arr[n - 1] + 1)
    DFS(0)
    if result:
        print("YES")
    else:
        print("NO")