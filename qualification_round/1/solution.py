import numpy as np
from scipy.special import factorial

def check_array(M):
    N = len(M)
    expected_sum = N * (N+1) / 2
    expected_prod = factorial(N, exact=True)

    c = 0
    r = 0
    for j in range(N):
        r += 0 if np.sum(M[j]) == expected_sum and np.prod(M[j]) == expected_prod else 1
        c += 0 if np.sum(M[:,j]) == expected_sum and np.prod(M[:,j]) == expected_prod else 1
    return np.trace(M), r, c

def check_array_slow(M):
    N = len(M)

    c = 0
    r = 0
    for j in range(N):
        for k in range(1,N+1):
            if not k in M[j]:
                r += 1
                break
        for k in range(1,N+1):
            if not k in M[:,j]:
                c += 1
                break
    return np.trace(M), r, c

T = int(input())

arrays = []

for i in range(T):
    N = int(input())
    M = np.zeros((N,N), dtype=np.int)
    for j in range(N):
        line = input()
        M[j] = np.array(line.split(' '), dtype=np.int)
    arrays.append(M)

for i, M in enumerate(arrays):
    k, r, c = check_array_slow(M)

    print("Case #{}: {} {} {}".format(i + 1, np.trace(M), r, c))