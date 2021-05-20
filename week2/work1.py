import time

A = [[1]*40]*40
B = [[1]*40]*40
n = len(A)
ans = [[0] * n for i in range(n)]

begin = time.time()

for i in range(n):
    for j in range(n):
        for k in range(n):
            ans[i][j] += A[i][k] * B[k][j]

end = time.time()
print("time: %.6f sec" % (end - begin))

# for item in ans:
#    print(*item)

