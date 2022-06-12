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
            print(-hq.heappop(arr))
    else:
        hq.heappush(arr,-n)

# 파이썬에서는 heaq과 관련된 함수를 지원하지만, 최소힙에 맞춰져 있다.
# 최대힙을 구현할 때는 살짝 변형만 주면 구현할 수 있다.
# - 부호를 곱해서 push를 하면 최소힙이 적용되어 4가 제일 큰 수로 push되면 루트에는 -4가 저장될 것이다.
# 그래서 출력할 때 - 부호를 다시 곱해주면 최대힙을 구현할 수 있게 된다.


