import heapq as hq

arr = []

while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(arr) == 0:
            print(-1)
        else:
            print(hq.heappop(arr))
    else:
        hq.heappush(arr,n)

# 파이썬에서는 heaq과 관련된 함수를 지원한다. heapq 라고 하는데,
# 리스트를 가지고 heappush 와 heappop을 하면 heap처럼 push와 pop을 한다.
# 최소힙은 부모노드가 자식노드 보다 작은 완전이진트리 자료형으로, 루트노드가 트리 중 가장 작다.

# 새로운 노드를 push할 때는, 마지막 level의 가장 오른쪽에 노드를 추가하고 upheap을 한다.
# upheap은 노드를 부모 노드와 비교하면서 자신이 더 작으면 루트노드와 swap하는 것. 그러다 자신의 위치를 찾게 된다.
# 노드를 pop할 때는 루트 노드가 pop되는데, 이 때 가장 밑 level의 가장 오른쪽 노드를 루트 노드에 넣고 downheap을 수행한다.
# downheap은 left right 자식노드와 비교한 후, 더 작은 자식노드와 swap을 하면서 자신의 위치를 찾아가는 것.

