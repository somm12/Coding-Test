def DFS(x):
    if x > 0:
        DFS(x-1)
        print(x,end=' ')

if __name__ == "__main__":
    n = int(input())
    DFS(n)

# 3을 입력해서 DFS를 호출한다면 1 2 3 이렇게 결과가 호출됨.
# 코드가 실행될 때 stack에 매개변수, 지역변수, 기억해야할 주소저장(다시 돌아올 때 어디로 와야하는지 표시)
# 이런식으로 스택에 저장된다. 한 번 호출될때 이 데이터들이 저장된 묶음을 stack frame이라고 한다.
