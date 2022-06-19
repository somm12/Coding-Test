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
# 두 부분집합의 원소들의 합이 같은 것이 존재할시 YES 출력 아니면 NO 출력을 하자.

# 나의 풀이: 부분집합을 DFS와 ch 배열로 1과 0으로 체크해서 만들고, 종료되는 시점의 부분집합의 합과
# 나머지 원소들의 합(차집합)을 비교해서 같다면 result 배열에 yes를 추가하는 방식으로 result 배열이 비어있지 않다면
# YES를 출력한다.
import sys
def dfs(L,sum):
    if sum > total // 2:
        return
    if L == n:
        if total - sum == sum:
            print("YES")
            sys.exit(0)
    else:
        dfs(L+1,sum + a[L])
        dfs(L+1, sum)

if __name__ == "__main__":
    n = int(input())
    a = list(map(int,input().split()))
    total = sum(arr)
    dfs(0,0)
    print("NO")
# 정답풀이: 부분집합의 합을 구하는 것이 목표이기 때문에 부분집합의 전체 모습까지 알 필요는 없다. 따라서
# ch 과 같은 체크배열은 필요없음. 
# 또한 주어진 배열이 항상 연속된 원소가 아니기 때문에 index를 매개변수로
# 전달해서 a[index]과 같이 접근한다. 또한 왼쪽 오른쪽 상태트리로 뻗어나가면서 매개변수로 sum을 구해서 전달할 
# 수 있다는 사실!!!! 
# 또한 (total - sum): 나머지 원소들의 합 == sum: 내가 구한 부분집합의 합으로 비교할 수 있다. 차집합쓸 필요 없다.
# 시간 복잡도 줄이는 방법! 결국 합이 같다는 말은 total//2 값으로 같다는 말이므로, sum을 더해나가면서
# 만약 sum이 total//2를 넘어간다면 더이상 재귀를 볼 필요 없이 바로 return시킨다.
# 또, 합이 동일한 경우가 존재할 시, 모든 재귀를 종료시키기 위해선 sys.exit(0)를 사용할 수 있다.

# 회고: 문제를 보자마자 빨리풀려고 했다가 좀 비효율적으로 풀 것 같다.
# 항상 문제를 풀기 전에는, 좀 더 종이에 그려보고 생각을 조금 더 해보면서 효율적으로 문제해결 할 수 있는 연습이
# 필요한 것 같음. 