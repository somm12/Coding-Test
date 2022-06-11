str1 = input()
str2 = input()
stringHash = dict()

for x in str1:
    stringHash[x] = stringHash.get(x,0) + 1

for x in str2:
    stringHash[x] = stringHash.get(x,0) - 1

for x in str1:
    if stringHash.get(x) > 0:
        print(stringHash)
        print("NO")
        break
else:
    print("YES")  

# 아나그램 딕셔너리 코드를 개선한 코드로, 딕셔너리를 하나만 사용하여 key값과 해당 개수의 value를 할당하고
# 두번째 문자열을 for문 반복을 통해 확인되면 -1을 하여 stringHash에 남은 key값이 0보다 크다면
# 아나그램이 아닌 것이다.
