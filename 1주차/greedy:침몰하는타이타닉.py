from collections import deque


n, limit = map(int,input().split())

people = list(map(int,input().split()))

people.sort()
people = deque(people)
count = 0

while people:
    if len(people) == 1:
        count += 1
        break
    if people[0] + people[-1] > limit:
        people.pop()
        count += 1
    else:
        people.popleft()
        people.pop()
        count += 1
print(count)

# 모든 사람이 구조되기 위해 필요한 최소!!의 배개수를 구하는 것이기 때문에 2명이 제한이니 2명이서 타고 가는것
# 을 지향 해야함.
# 최소가 되려면! 제일 가벼운 사람 과 무거운 사람이 함께 배에 타는 것이 같이 제한 내로 배를 탈 수 있는 확률이 크다.
# 따라서 sort 를 먼저하고, pop을 이용해서 탈출한 사람은 빠지게 한다.
# 주의해야할 것은, 1명이 남았을 때는 바로 count를 세고 break문으로 빠져나와야함.

# list를 이용하면 pop을 했을때 뒤의 원소들이 앞당겨지는 연산을 수행해야함 -> 비효율적!
# 따라서 deque 라는 자료구조를 이용하면 list와 같은 연산을 수행하지 않아도 pop을 했을 때 자동으로 
# 그 다음 원소를 첫 원소로 포인터가 가리키게 됨. *** 맨 앞 원소 추출시 popleft 사용.