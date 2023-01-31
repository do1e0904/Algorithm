#정답
n=int(input())
print(min(n//125+n//25+n//5,n//2))

#1 오답, 25의 배수, 125의 배수는 각각 5가 두번, 세번, 나오므로 10이 만들어질 경우가 더 생김
n=int(input())
print(min(n//5,n//2))
