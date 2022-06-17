stack = []
def decToBin(x):
    if x != 0:
        stack.append(x % 2)
        x = x // 2
        decToBin(x)

def printResult():
    if stack:
        x = stack.pop()
        print(x, end = '')
        printResult()

if __name__ == "__main__":
    n = int(input())
    decToBin(n)
    printResult()

# 나의 풀이 재귀와 스택을 이용해서 답을 출력함.

def decToBin2(x):
    if x == 0:
        return
    else:
        decToBin2(x // 2)
        print(x % 2, end='')

# 정답풀이 재귀의 특징을 이용해서 출력도 함께하는 방법의 풀이다. => 재귀와스택에서 배운 것 처럼 
# 재귀가 실행될 때 컴퓨터에서 스택 내에 데이터를 저장하고 마지막 저장했던 코드부분 주소로 다시 되돌아가기 때문에 재귀만 이용하는 것이 더 효율적!