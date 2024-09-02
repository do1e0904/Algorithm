import heapq
import sys
input = sys.stdin.readline

heap = []
n = int(input())
for _ in range(n):
    tmp = int(input())
    if tmp == 0:
        if not heap:
            print('0')
        else:
            ans = heapq.heappop(heap)
            print(ans[1])
    else:
        heapq.heappush(heap,[abs(tmp),tmp])
