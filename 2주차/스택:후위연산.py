arr = input()
stack = []

for value in arr:
    if value.isdecimal():
        stack.append(value)
    else:
        b = int(stack.pop())
        a = int(stack.pop())
        
        if value == '+':
            result = a + b
        elif value == '-':
            result = a - b
        elif value == '*':
            result = a * b
        elif value == '/':
            result = a // b
        stack.append(result)

print(stack[0])

# 후위연산식을 연산해서 결과를 출력하는 코드
# 숫자는 stack에 넣고 연산자를 만나면 앞의 두 숫자를 pop해서 계산결과를 다시 append한다.
# 마지막 남은 숫자 하나가 최종 계산 결과다.