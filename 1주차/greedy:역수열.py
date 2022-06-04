n = int(input())

arr = list(map(int,input().split()))
originalArr = [0] * n

for i in range(n):
    count = 0
    for k in range(n):
        if originalArr[k] == 0:
            count += 1
        if count > arr[i] and originalArr[k] == 0:
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

# **** 중요한 것은 1의 위치를 찾는다고 할 때, 앞의 0의 개수를 증가시키면서 5 가 되고 && original 수열의
# 해당 위치의 원소가 0이여야(아직 비었을때) 원래 수열의 위치를 정확하게 찾을 수 있다.


# count 안쓰는 방법
# 역수열의 수를 이용해서 1씩 빼서 0이 되는 순간이 바로 해당 원소의 인덱스위치.
# n = int(input())

# arr = list(map(int,input().split()))
# originalArr = [0] * n

# for i in range(n):
#     for k in range(n):
#         if arr[i] == 0 and originalArr[k] == 0:
#             originalArr[k] = i + 1
#             break
#         elif originalArr[k] == 0:
#             arr[i] -= 1

# for value in originalArr:
#     print(value, end=' ')
