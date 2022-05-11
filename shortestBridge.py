A = [[0,1,0],[0,0,0],[0,0,1]]
#A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
r = list()
for l in A:
    if (len(l) - sum(l)) > 0:
        r.append(len(l) - sum(l))

if (len(A[0])) < 3:
    print(min(r))
else:
    print(min(r)-1)
