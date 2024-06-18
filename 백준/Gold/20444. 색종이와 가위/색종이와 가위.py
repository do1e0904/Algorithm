# *s3..g4 %ko !@$me

def cutPaper(left, right):
    if left >= right:
        print("NO")
    else:
        middle = (left + right) // 2
        if (left == middle or right == middle) and (k - n != 1):
            print("NO")
            return
        paper = (middle + 1) * (n - middle + 1)
        #print(left, right, middle, middle+1, n-middle+1, paper)
        if paper == k:
            print("YES")
        elif paper < k:
            left = middle
            cutPaper(left, right)
        elif paper > k:
            right = middle
            cutPaper(left, right)

n, k = map(int, input().split())
cutPaper(0, n)
