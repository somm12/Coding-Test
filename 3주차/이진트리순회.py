def DFS(v):
    if v > 7:
        return
    else:
        print(v, end=' ')
        DFS(2 * v)
        DFS(2 * v + 1)

if __name__ == "__main__":
    DFS(1)

# 위는 전위순회로, 부모 왼 오 순서로 순회한다.
# 중위순회는 왼 부모 오 순서로 순회하고, => print의 위치는 else문에서 2번째
# 후위순회는 왼 오 부모 순서로 순회한다. => print의 위치는 else문에서 마지막 줄