n, m = map(int, input().split())
h = list(map(int, input().split()))
a = list(map(int, input().split()))
h.sort()
a.sort()
print(h[len(h)-1] + a[len(a)-1])
