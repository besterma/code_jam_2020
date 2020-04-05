import numpy as np


def solve(i, N, K):
    possible, trace = check_if_possible(N, K)

    if not possible:
        print("Case #{}: {}".format(i + 1, "IMPOSSIBLE"))
        return
    else:
        print("Case #{}: {}".format(i + 1, "POSSIBLE"))
        matrix = create_matrix(trace)
        for j in range(N):
            print(" ".join(map(str, matrix[j])))


def create_matrix(trace):
    N = len(trace)
    matrix = np.zeros((N, N), dtype=np.int)
    for i in range(N):
        matrix[i] = np.array([(trace[n]-i-1 + n) % N + 1 for n in range(N)])

    return matrix


def check_if_possible(N, K):
    if K % N == 0:
        return True, [K // N for _ in range(N)]

    known_possibles = [i * N for i in range(1, N + 1)]
    pos = 0
    while K > known_possibles[pos]:
        pos += 1
    if K - known_possibles[pos - 1] == known_possibles[pos] - K and K - known_possibles[pos - 1] % 2 == 0:
        starter = [known_possibles[pos-1] // N for _ in range(N)]

        return True,
    else:
        return False, None


def main():
    T = int(input())
    inputs = []
    for _ in range(T):
        inputs.append(input())

    for i, kn in range(T):
        N, K = list(map(int, kn.split()))


if __name__ == '__main__':
    main()
