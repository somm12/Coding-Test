a = []
def DFS(n):
    if n > 3:
        return
    else:
       a.append(n)
       DFS(n+1)
       print(a)
       a.pop()
       DFS(n+1)

DFS(1) 