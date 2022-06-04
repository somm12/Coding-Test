n = int(input())

arr = list(map(int,input().split()))
originalArr = [0] * n

for i in range(n):
    count = 0
    for k in range(n):
        if originalArr[k] == 0:
            count += 1
        if count > arr[i]:
            originalArr[k] = i + 1
            break

for value in originalArr:
    print(value, end=' ')

# 1 ~ n 까지 모든 수를 가지고 있는 수열 4 8 6 2 5 1 3 7 의 역수열은
# 5 3 4 0 2 1 1 0 이다. 역수열은 원래 수열에서 읽은 수 4보다 큰 수가 앞에 몇 개 있는지 나타낸 것.
# ex) 4보다 큰 수는 4 앞에서 1개도 없음. 따라서 역수열의 4번째 원소는 0 .

# 역수열을 입력 받고, 원래 수열을 찾아내는 것이 목표.
# 5 3 4 0 2 1 1 0
# 1 2 3 4 5 6 7 8 => 즉 원래수열은 차례대로 1보다 큰 원소가 1 앞에 5개 있고, 2는 3개가 있고 등등
# 원래 수열을 0으로 초기화하여 0의 개수를 증가시키면서 원래수열의 모습을 찾아나간다.