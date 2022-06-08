arr = input()
stack = []
result = 0

for i in range(len(arr)):
    if arr[i] == '(':
        stack.append(arr[i])
    else:
        stack.pop()
        if arr[i-1] == '(':
            result += len(stack)
        else:
            result += 1
print(result)

# 레이저로 쇠막대기를 자르려고 한다. 총 쇠막대기 조각 수를 구하자.
# 여는 괄호와 가장 인접한 닫는 괄호 () 이 부분이 레이저이고 나머지 부분은 쇠막대기 이다.
# 문제를 천천히 이해하면서 문제가 알려주는 그대로 손으로 쓰면서 또는 그림을 그려가면서 문제 풀이를 생각해보자.

# 여는 괄호는 stack에 추가, 만일 닫는 괄호 바로 앞에 여는 괄호가 있다면 레이저를 만나는 것이므로,
# 스택에 남은 여는 괄호 즉, 막대기 개수를 센다.
# 그 이후 닫는 괄호는 막대기가 잘려진 뒷부분 +1 을 해준다.