import sys
s = list(sys.stdin.readline().strip())
result = []
stack = []

for i in range(len(s)):
    if s[i] == ')':
        while stack[len(stack)-1] != '(':
            result.append(stack.pop())
        stack.pop()
    elif s[i] == '(':
        stack.append(s[i])
    elif s[i] == '+' or s[i] == '-':
        while stack:
            if stack[len(stack)-1] == '*' or stack[len(stack)-1] == '/' or stack[len(stack)-1] == '+' or stack[len(stack)-1] == '-':
                result.append(stack.pop())
            else:
                break
        stack.append(s[i])
    elif s[i] == '*' or s[i] == '/':
        while stack:
            if stack[len(stack)-1] == '*' or stack[len(stack)-1] == '/':
                result.append(stack.pop())
            else:
                break
        stack.append(s[i])
    else:
        result.append(s[i])
while stack:
    result.append(stack.pop())
print(''.join(result))
        
        
