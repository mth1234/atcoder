X, A, D, N = tuple(map(int, input().split()))

first = 0
last = N - 1
first_dist = 0
last_dist = 0
while(True):
    first_dist = abs(A + D * first - X)
    last_dist = abs(A + D * last - X)

    if abs(first - last) <= 1:
        break
    elif first_dist < last_dist:
        last -= int((last - first) / 2)
    else:
        first += int((last - first) / 2)

print(min(first_dist, last_dist))