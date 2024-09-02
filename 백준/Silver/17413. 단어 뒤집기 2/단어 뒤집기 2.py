from collections import deque
import sys
input = sys.stdin.readline
s = list(input().rstrip())
stack=[]
queue=deque()
i=0
while i < len(s):
    if s[i] == '<':
        while stack:
            print(stack.pop(),end='')
        while s[i] != '>':
            queue.append(s[i])
            i+=1
        queue.append(s[i])
        i+=1
        while queue:
            print(queue.popleft(),end='')
    elif s[i] == ' ':
        while stack:
            print(stack.pop(),end='')
        print(end=' ')
        i +=1
    else:
        stack.append(s[i])
        i+=1
while stack:
    print(stack.pop(),end='')