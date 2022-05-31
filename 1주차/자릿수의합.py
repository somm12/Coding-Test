n = int(input())
arr = list(map(int,input().split()))

def digitSum(x):
    result = 0
    while x > 0:
        result += x % 10
        x = x // 10
    # 두번째 방법
    # for i in str(x):
    #     result += int(i)
    return result

maxDigitSum = -1
for i  in arr:
    totalSum = digitSum(i)
    if maxDigitSum < totalSum:
        maxDigitSum = totalSum
        maxNumber = i

print(maxNumber)