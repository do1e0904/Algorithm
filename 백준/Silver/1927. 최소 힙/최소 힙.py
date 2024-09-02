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
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap,tmp)