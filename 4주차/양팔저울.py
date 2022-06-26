def DFS(L,sum):
    global res
    if L == n:
        if 0 < sum <= s:
            res.add(sum)
    else:
        DFS(L+1,sum + G[L])
        DFS(L+1,sum - G[L])
        DFS(L+1,sum)

if __name__ == "__main__":
    n = int(input())
    G = list(map(int,input().split()))
    s = sum(G)
    res = set()
    DFS(0,0)
    print(s - len(res))

# 문제: 주어진 n개의 추와 추의 종류를 입력받고 양쪽저울을 한 번만 사용하여 (그릇은 무게가 0)
# 그릇에 담을 수 없는 물의 무게가 몇 가지 인지 구하자. 최대 sum(추 종류 합)까지 만들 수 있음.

# 문제가 양쪽저울을 이용해서 푸는 것이기 때문에 저울에 추를 하나 둘 달고 물 무게를 생각해보자.
# 트리를 그려나가 보자면, 처음 0부터 시작해서 왼쪽에 추를 달면 추 무게를 더하고 오른쪽에 추를 달면 무게를 빼준다.
# 그리고 추를 사용안하는 경우가 있으니 그대로 둔다. 총 이렇게 3가지 경우가 있고
# 반복적으로 3번씩 가지가 뻗어나간다. 따라서 재귀호출을 3개로 만들 수 있다는 구상을 할 수 있다.

# 계산을 반복적으로 하다보면 음수가 나오는 경우 있는데, 이 경우는 결국 양쪽 저울을 써서 대칭이 되기 때문에
# -1 이 있다면 1 이 있고 -5가 있다면 5가 나온다. 따라서 가지수를 더해나갈 때, 양수인 것만 더하면 된다.

# 추 n개를 모두 더했을 때까지가 모든 경우를 포함한(어떤 추는 쓰고 안쓰고 또는 오른쪽 왼쪽에 달아서 만든 무게 다 포함)
# 최대 레벨이기 때문에 L == n일 때가 종료조건이며, 이 때 만들 수 있는 무게를 더한다.

