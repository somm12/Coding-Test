arr = input()
answer = ""
for i in arr:
    if i.isnumeric():
        answer += i
answer = int(answer)
print(answer)

#약수의 개수
numOfDivisor = 0
for i in range(1, answer+ 1):
    if answer % i == 0:
        numOfDivisor += 1
print(numOfDivisor)

# 숫자인지 아닌지 판별해주는 함수 isnumeric, isdigit, isdecimal