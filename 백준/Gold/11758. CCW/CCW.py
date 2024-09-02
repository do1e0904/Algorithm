p1_x, p1_y = map(int, input().split())
p2_x, p2_y = map(int, input().split())
p3_x, p3_y = map(int, input().split())

if p1_x != p2_x:
    delta1 = (p1_y - p2_y) / (p1_x - p2_x)
else:
    delta1 = 'INF'

if p2_x != p3_x:
    delta2 = (p2_y - p3_y) / (p2_x - p3_x)
else:
    delta2 = 'INF'

if delta1 != 'INF' and delta1 != 0 and delta2 != 'INF' and delta2 != 0:
    D = delta1 * delta2
    if delta1 == delta2:
        print(0)
    elif D == -1:
        if p2_x > p1_x and p2_y > p1_y:
            if p3_x < p2_x:
                print(1)
            else:
                print(-1)
        elif p2_x < p1_x and p2_y > p1_y:
            if p3_x < p2_x:
                print(1)
            else:
                print(-1)
        elif p2_x < p1_x and p2_y < p1_y:
            if p3_x > p2_x:
                print(1)
            else:
                print(-1)
        elif p2_x > p1_x and p2_y < p1_y:
            if p3_x > p2_x:
                print(1)
            else:
                print(-1)
    elif D > 0:
        if p2_x > p1_x and p2_y > p1_y:
            if (p3_x > p2_x and p3_y > p2_y and delta1 < delta2) or (p3_x < p2_x and p3_y < p2_y and delta1 > delta2):
                print(1)
            else:
                print(-1)
        elif p2_x < p1_x and p2_y > p1_y:
            if (p3_x > p2_x and p3_y < p2_y and delta1 > delta2) or (p3_x < p2_x and p3_y > p2_y and delta1 < delta2):
                print(1)
            else:
                print(-1)
        elif p2_x < p1_x and p2_y < p1_y:
            if (p3_x > p2_x and p3_y > p2_y and delta1 > delta2) or (p3_x < p2_x and p3_y < p2_y and delta1 < delta2):
                print(1)
            else:
                print(-1)
        elif p2_x > p1_x and p2_y < p1_y:
            if (p3_x > p2_x and p3_y < p2_y and delta1 < delta2) or (p3_x < p2_x and p3_y > p2_y and delta1 > delta2):
                print(1)
            else:
                print(-1)
    elif D < 0:
        if p2_y > p1_y:
            if p3_x < p2_x:
                print(1)
            else:
                print(-1)
        else:
            if p3_x > p2_x:
                print(1)
            else:
                print(-1)
else:
    if delta1 == delta2:
        print(0)
    elif delta1 == 'INF':
        if p3_x < p2_x:
            print(1)
        else:
            print(-1)
    elif delta1 == 0:
        if p3_y > p2_y:
            print(1)
        else:
            print(-1)
    elif delta2 == 'INF':
        if p1_x < p2_x:
            print(1)
        else:
            print(-1)
    elif delta2 == 0:
        if p1_y > p2_y:
            print(1)
        else:
            print(-1)