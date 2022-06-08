number , m = map(int,input().split())
number = list(map(int,str(number)))

stack = []

for value in number:
    while stack and m > 0 and stack[-1] < value:
        stack.pop()
        m -= 1
    stack.append(value)

if m != 0:
    stack = stack[:-m]

for value in stack:
    print(value, end='')

# 주어진 수 number에서 주어진 수 m개의 수를 제거할 때 가장 큰 수를 만들어야한다.
# 여기서 포인트는 가장 큰 수를 만들어야하므로 앞자리수가 커야하고 => 숫자를 하나씩 읽어나갈 때 자기자신보다 
# 작은 수가 앞에 있으면 큰 수가 될 수 없다. 그래서 그 수를 제거해야함.
# 만약 그렇게 제거 했을 때 m개가 0이 되지 않았다면 남은 뒤의 숫자 m개를 제거한다. 슬라이싱 기능을 활용해서
# -m 번째 숫자 전까의 수를 출력한다.

# number = list(map(int,str(number))) 이 부분은 숫자인 number를 str로 각 문자로 바꾸어 map을 이용해
# 다시 모든 원쇠를 숫자로 변환한 리스트로 만든다.