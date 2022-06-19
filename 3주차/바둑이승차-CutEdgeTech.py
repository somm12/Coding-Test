
def DFS(index, sum):
    global max
    if sum > C:
        return
    if index == N:
        if sum > max:
            max = sum
    else:
        DFS(index + 1, sum + arr[index])
        DFS(index + 1, sum)

if __name__ == "__main__":
    C, N = map(int,input().split())
    arr = []
    max = 0
    for _ in range(N):
        arr.append(int(input()))

    DFS(0,0)
    print(max)
# 나의 풀이
# 바둑이들을 무게 C가 넘지 않게 최대한 무겁게 트럭에 싣자.
# DFS를 이용해서 매개변수를 sum으로 전달해서 C를 넘으면 return, max를 전역변수로 두어서 sum이 max보다 크면
# max를 update한다.
