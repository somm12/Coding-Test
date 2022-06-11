str1 = list(input())
str2 = list(input())

for i in range(len(str2)):
    if str2[i] in str1:
        str1.pop(str1.index(str2[i]))
if len(str1) > 0:
    print("NO")
else:
    print("YES")

# 리스트를 이용해서 해당 알파벳이 존재하면 pop을 통해 한 문자라도 str1에 남으면 NO

a = input()
b = input()
#알파벳 개수 26개 대문자 소문자 모두 52개
str1[0] = [0] * 52 
str2[0] = [0] * 52
# 대문자는 index가 0 ~ 25, 소문자는 26 ~ 51로 만들고자함.
for x in a:
    if x.isupper():
        str1[ord(x) - 65] += 1
    else:
        str1[ord(x) - 71] += 1

for x in b:
    if x.isupper():
        str2[ord(x) - 65] += 1
    else:
        str2[ord(x) - 71] += 1

for i in range(52):
    if str1[i] != str2[i]:
        print("NO")
        break
else:
    print("YES")

# 정답풀이 : 정말 c++ 처럼 풀어보자. 
# 같은지 비교할 때 if str1 == str2 를 사용해도 되지만 최대한 c++ 처럼 하기로 했으니
# for문을 이용해서 비교한다.