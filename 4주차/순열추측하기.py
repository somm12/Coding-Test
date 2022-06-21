import sys
def pascalSum(res):
    temp = []
    while len(res) != 1:
        for i in range(len(res)-1):
            temp.append(res[i] + res[i+1])
        res = temp.copy()
        temp = []
    return res[0]

def DFS(L):
    global cnt, res
    if L == n:
        result = pascalSum(res)
        if result == F:
            for i in res:
                print(i, end= ' ')
            sys.exit(0)
    else:
        for i in range(1,n+1):
            if i not in res[:L]:
                res[L] = i
                DFS(L+1)

if __name__ == "__main__":
    n, F = map(int,input().split())
    res = [0] * n
    cnt = 0    
    DFS(0)
    print(cnt)

# 순열구하기에서 주어진 1부터 n 까지의 연속된 숫자의 수열 형태을 추측하는 문제로,
# 파스칼 삼각형을 이용하여 마지막 숫자 F를 가지고 수열을 추측하라.
# n 이 4이고 F가 16이면, 1 2 3 4의 다른 형태의 수열에서 파스칼 삼각형의 합이 16이 되게 하도록 수열을 구하는 것

# 나의 풀이: 순열구하기 부분과 비슷하기 때문에 n개의 숫자가 선택되어 수열이 만들어지면 
# 파스칼 삼각형의 합을 구하는 함수를 호출해서 그 합이 F인지 check하는 방식으로 구현했다.
# 단점: 순열을 구할 때 마다 일일이 파스칼을 연산하면 비효율적일 것.




def DFS(L,sum):
    global res
    if L == n and sum == F:
        for i in res:
            print(i, end= ' ')
        sys.exit(0)
    else:
        for i in range(1,n+1):
            if i not in res[:L]:
                res[L] = i
                DFS(L+1,sum+(b[L]*res[L]))

if __name__ == "__main__":
    n, F = map(int,input().split())
    res = [0] * n
    b = [1] * n
    sum = 0
    for i in range(1,n):
        b[i] = (b[i-1] * (n-i)) // i
    DFS(0,0)
# 정답 풀이: 순열은 일일이 찾아야겠지만 그 순열의 파스칼 합은 효율적으로 계산할 수 있다.
# 파스칼의 합을 잘 보면 **이항계수 규칙이 보이기 때문에 b라는 n크기의 배열을 만들어서 이항계수를 넣은뒤
# 해당 순열 배열과 곱하여 계산하면 원하는 파스칼 합이 나오게 된다. ex) b = [1,3,3,1], arr = [3,1,2,4]
# 파스칼 합: 1*3 +3*1 + 3*2 + 1*4 = 16.
# 이항계수는  b[i] = (b[i-1] * (n-i)) // i 와 같이 할당을 하고 sum은 매개변수로 전달해서 축적해서 더해나가며 체크할 수 있다.

