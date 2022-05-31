n = int(input())
arr = list(map(int,input().split()))
def reverse(x):
    result = 0 
    while x > 0:
        temp = x % 10
        result += result * 10 + temp
        x = x // 10
def isPrime(x):
    result = 0
    if x == 1:
        return False
    for i in range(2,x//2+1):
        if x % i == 0:
            return False
    # 위의 for문이 중간에 break가 되지 않고 정상적으로 종료가 됐을 때.
    else:
        return True
for value in arr:
    reversedValue = reverse(value)
    checkIfPrime = isPrime(reversedValue)
    if checkIfPrime == True:
        print(value)

# 소수란 자기 자신과 1 만 약수를 가진 수로, 2부터 그 전까지 수로 나누었을 때 떨어졌는지 확인.
# 하지만 계산과정을 줄이기 위해서 target//2 까지만 나눈다. 예시로 18은 1*18,2*9,3*6 인데 1과 자기자신을 제외하고 2와 곱해지는 수 9가 제일 큰 약수일 테니 거기까지만 확인한다.