
from turtle import st


arr = input()
stack = []
result = ""
operator = ['+','-','*','/','(',')']
priority = [0,0,1,1,2,2]

for value in arr:
    if value.isnumeric():
        result += value
    else:
        if len(stack) == 0:
            stack.append(value)
        else:
            while priority[operator.index(value)] <= priority[operator.index(stack[-1])]:
                print(value)
                if stack[-1] == '(':
                    stack.append(value)
                    break
                elif stack[-1] == ')':
                    stack.pop()
                    while stack[-1] != '(':
                        result += stack.pop()
                    stack.pop()
                else:
                    result += stack.pop()
                if len(stack) == 0:
                    stack.append(value)
                    break
            else:
                stack.append(value)
print(stack)
if len(stack) > 0:
    while len(stack) != 0:
        value = stack.pop()
        if value != '(' and value != ')':
            result += value
print(result)

### 문제풀이
arr = input()
result = ''
stack = []

for value in arr:
    if value.isdecimal():
        result += value
    else:
        if value == '(':
            stack.append(value)
        elif value == '+' or value == '-':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(value)
        elif value == '*' or value == '/':
            while stack and (stack [-1] != '*' or stack[-1] != '/'):
                stack.pop()
            stack.append(value)
        elif value == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
while stack:
    result += stack.pop()
print(result)

## 중위식을 후위식으로 바꾸는 코드
# 연산자의 개수가 정해져 있기 때문에 if else 문을 써도 괜찮다 그리고 while 에서도 and or 조건문을 
# 써도 괜찮으니 적극적으로 활용하자. 안써서 더 복잡하고 읽기 힘든 코드는 좋지 않다.
# 우선순위가 같은 연산자끼리 묶어서 if elif 조건문을 사용해서 그에 따른
# 연산처리를 만들 수 있다.

# + 와 -는 가장 우선순위가 낮으므로 ( 괄호가 없다면 pop을 계속해준다. 다만 pop을 해주기 때문에 stack이 empty가
# 되기 전까지 실행하기 위해서 while stack 도 함께 조건으로 걸어준다

# * 와 / 는 앞에 먼저 들어온 * 또는 / 연산자를 만났을 때 pop 해야하므로 조건을 만족할 때까지 pop.

# ) 를 만나면 괄호식이 끝났기 때문에, 괄호식은 우선순위가 제일 높기 때문에
#  그 다음 어떤 연산자가 들어와도 pop이 돼야한다. 따라서
# ( 여는 괄호를 만날 때까지 모두 pop을 한다.

# 잊지 말고 우선순위에 따라 pop을 해주면 꼭 해당 value를 append해야한다. 항상 append하기 전에 검사만 했으니
# append 되지 않았다는 사실!

# 마지막으로 stack에 남은 연산자들은 순서대로 pop한다.