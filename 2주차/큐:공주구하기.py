from collections import deque

n ,k = map(int,input().split())
princeArr = [i for i in range(1,n+1)]
princeArr = deque(princeArr)

while len(princeArr) != 1:
    for i in range(1, k+1):
        if i == k:
            princeArr.popleft()
        else:
            princeArr.append(princeArr.popleft())

print(princeArr[0])

# 큐는 FIFO(First In First Out)로 먼저 들어간 원소가 먼저 나오는 자료구조.
# 파이썬에서는 deque라는 구조를 지원, 왼쪽과 오른쪽 모두에서 pop과 append를 할 수 있다.
# 왼쪽에는 popleft, appendleft 기능, 오른쪽에는 리스트와 같은 pop과 append기능이 있다.
# 일반적으로 큐 자료구조 기능을 이용해서 deque를 사용하려면 popleft와 append 기능을 사용하면 된다.

# 문제풀이
# k 번째 원소가 제외되고 그 이후부터 다시 1부터 세어서 k번째인 원소를 제외시키고 마지막 하나 남은 원소를 알아낸다.
# k 번째 원소 다음부터 1 번째로 세기 때문에 k - 1 번째까지 원소들은 빼내어서 다시 append해야한다.