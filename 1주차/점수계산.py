arr = list(map(int,input().split()))
check = 0
result = 0
for score in arr:
    if score == 1:
        check += 1
        result += check
    else:
        check = 0
    
print(result)