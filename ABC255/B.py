from math import sqrt

N, K = tuple(map(int, input().split()))

A = list(map(int, input().split()))

P = []

for i in range(N):
    P.append(tuple(map(int, input().split())))

RP = []
NP = []

for i in range(len(P)):
    if (i + 1) in A:
        RP.append(P[i])
    else:
        NP.append(P[i])


dist_matrix = [[] for _ in range(K)]
count = 0
for p1 in RP:
    for p2 in NP:
        dist_matrix[count].append(sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2))
    
    count += 1

dist_min_list = []
for i in range(len(NP)):
    dist_min_list.append(min([r[i] for r in dist_matrix]))

print(max(dist_min_list))