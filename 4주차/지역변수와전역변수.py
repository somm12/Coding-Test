def DFS1():
    # 함수는 전역변수와 지역변수의 이름이 같을 때 지역변수를 우선으로 둔다.
    cnt = 3
    print(cnt)

def DFS2():
    global cnt
    # 여기서 만약 global 선언이 없다면 에러 발생, cnt = cnt + 1 여기서 이 함수의 지역변수가 생기지만 cnt 값을 아직 할당 안해줬음.
    if cnt == 5:
        cnt = cnt + 1
        print(cnt)
if __name__ == "__main__":
    # main안에 있는 변수들은 전역변수이다.
    cnt = 5
    DFS1()
    DFS2()
    print(cnt)

# ** 즉 함수 내에서 'a =' 을 한 순간! 그 함수 내의 a를 모두 지역변수로 인식.