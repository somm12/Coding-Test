n = int(input())
result = 0

for i in range(n):
    a, b, c = map(int,input().split())

    if a == b and b == c:
        money = 10000 + a*1000
    elif a == b or a == c:
        money = 1000 + (a*100)
    elif b == c:
        money = 1000 (b*100)
    else:
        money = c*100
    if money > result:
        result = money
print(result)
# if elif else 문을 사용할 때는 가장 조건이 좋은 순으로 써야한다. 만약 a == b or a == c가 처음으로 배치
# 된다면 세 수가 모두 같을 때 경우가 적용되버려서 틀린 답을 낼 수 있다.