# def DFS(L):
#     global cnt, res
#     count = 0
#     for i in res:
#         if i > 0 :
#             count += 1
#     if count < m and L > n:
#         return
#     if count == m:
#         for k in range(1,n+1):
#             if res[k] > 0:
#                 print(k, end=' ')
#         cnt += 1
#         print()

#     else:
#         res[L] = 1
#         DFS(L+1)
#         res[L] = 0
#         DFS(L+1)
# if __name__ == "__main__":
#     n, m = map(int,input().split())
#     res = [0] * (n+1)
#     cnt = 0
#     DFS(1)
#     print(cnt)

# 나의 풀이: 어떻게 문제를 풀지는 부분집합 구하기에서 응용을 하면 된다. 하지만 종료조건을 하나 더 찾는데 오래 걸렸다.
# 조합은 순열과 다르게 1 2 , 2 1 이나 같은 답이다. 그래서 res배열로 체크하면서 원소가 1인 것의 개수가 m개 일 때 조합을 출력하는 방식으로 구현.
# 하지만 순열과 다르게 for문으로 n까지 호출하는 것이 아니기 때문에 n을 넘어가는 재귀 호출까지 갈 수 있다!!!!
# 여기서 만약 아직 m개 뽑지 않은 상태 && n 을 넘어가버리면 조건에 맞는 답을 못찾고 index out of range 오류가 생기기 때문에
# 이를 꼭 종료조건에 포함 시키자!!!!

def dfs(L,s):
    global m, res, cnt
    
    if L == m:
        for i in res:
            print(i, end=' ')
        print()
        cnt += 1
    else:
        for i in range(s,n+1):
            res[L] = i
            dfs(L+1,i+1)

if __name__ == "__main__":
    n, m = map(int,input().split())
    cnt = 0
    res = [0] * m
    dfs(0,1)
    print(cnt)
# 정답풀이: 내가 푼 방법은 부분집합을 이용한 것이고, 조금 복잡할 수 있다.
# 순열구하기과 조금 비슷한 트리 구조로 조합을 구할 수 있다.
# 일반적으로 조합을 구할 때 1 2 3 4 5를 처음에
# 1 2 , 1 3 , 1 4, 1 5
# 2 3 , 2 4 ,2 5
# 3 4, 3 5
# 4 5
# 이렇게 구한다. 여기서 규칙을 찾아서 dfs 매개변수에 s 라는 start를 의미하는 매개변수를
# 둬서 1을 중심으로 끝까지 뽑고 나서 그 다음 2부터 끝까지 중에서 고를 수 있다. 
# 그래서 res[L] = i 여기서 i는 뽑은 수이기 때문에 재귀 호출시 dfs(L+1, i+1) 그 숫자를 제외한 다음 부터
# 골라야한 다는 의미.