import sys
import numpy as np


def solve(B):
    if B == 10:
        solution = []
        for i in range(B):
            solution.append(request_index(i))
        print("".join(map(lambda x: "1" if x else "0", solution)))
        sys.stdout.flush()
        if input() == "Y":
            return 0
        else:
            return 1
    else:
        our_list = []
        for i in range(B//2):
            a = request_index(i)
            b = request_index(B - i - 1)
            our_list.append((a, a == b))

        # our_list = [(False, True), (False, False), (True, True), (True, False), (False, True)]

        index = 0
        nr_requests = 0
        values = np.zeros(B, dtype=np.bool)
        temp_index_equal = None
        temp_index_unequal = None
        while index+5 <= len(our_list):
            if nr_requests == 9:
                request_index(0)
                nr_requests += 1
                # security measure
            if nr_requests == 10:
                temp_equal = np.array(list(map(lambda x: x[1], our_list[:index])))
                if temp_index_equal is None and (np.all(temp_equal) or not np.any(temp_equal)):
                    value = request_index(index-1)
                    if value != values[index-1]:
                        values = np.invert(values)
                    nr_requests = 1
                else:
                    if temp_index_equal is None:
                        temp_index_equal = np.where(temp_equal)[0][0]
                        temp_index_unequal = np.where(np.invert(temp_equal))[0][0]

                    equal_pair = (values[temp_index_equal], request_index(temp_index_equal))
                    unequal_pair = (values[temp_index_unequal], request_index(temp_index_unequal))
                    if np.equal(*equal_pair) and np.equal(*unequal_pair):
                        pass
                        # nothing happened
                    elif np.equal(*equal_pair) and not np.equal(*unequal_pair):
                        values = np.flip(values)
                    elif not np.equal(*equal_pair) and np.equal(*unequal_pair):
                        values = np.flip(np.invert(values))
                    else:
                        values = np.invert(values)
                    nr_requests = 2

            temp_equal = np.array(list(map(lambda x: x[1], our_list[index:index+5])))
            temp_values = np.array(list(map(lambda x: x[0], our_list[index:index+5])))

            a = request_index(index)
            if np.all(temp_equal) or not np.any(temp_equal):
                if temp_values[0] != a:
                    temp_values = np.invert(temp_values)
                values[index:index+5] = temp_values
                if not np.any(temp_equal):
                    temp_values = np.invert(temp_values)
                temp_values = np.flip(temp_values)
                if index == 0:
                    values[-index - 5:] = temp_values
                else:
                    values[-index - 5: - index] = temp_values
                nr_requests += 1
            else:
                diff_index = 1
                while temp_equal[0] == temp_equal[diff_index]:
                    diff_index += 1
                b = request_index(index + diff_index)
                if temp_equal[0]:
                    equal_pair = (temp_values[0], a)
                    unequal_pair = (temp_values[diff_index], b)
                    temp_index_equal = index
                    temp_index_unequal = index+diff_index
                else:
                    equal_pair = (temp_values[diff_index], b)
                    unequal_pair = (temp_values[0], a)
                    temp_index_equal = index+diff_index
                    temp_index_unequal = index
                if np.equal(*equal_pair) and np.equal(*unequal_pair):
                    pass
                    # nothing happened
                elif np.equal(*equal_pair) and not np.equal(*unequal_pair):
                    temp_values = np.array(list(map(lambda x: x[0] if x[1] else not x[0],
                                                    zip(temp_values, temp_equal))))  # this is basically the flip
                elif not np.equal(*equal_pair) and np.equal(*unequal_pair):
                    #temp_values = np.flip(temp_values)
                    temp_values = np.array(list(map(lambda x: x[0] if x[1] else not x[0],
                                                    zip(temp_values, temp_equal)))) # this is basically the flip
                    temp_values = np.invert(temp_values)
                else:
                    temp_values = np.invert(temp_values)
                values[index:index + 5] = temp_values
                temp_values = np.flip(np.array(list(map(lambda x: x[0] if x[1] else not x[0], zip(temp_values, temp_equal)))))
                if index == 0:
                    values[-index - 5:] = temp_values
                else:
                    values[-index - 5: - index] = temp_values
                nr_requests += 2

            index += 5

        for i in range(B//2):
            assert (values[i] == values[B-i-1]) == our_list[i][1], i
        print("".join(map(lambda x: "1" if x else "0", values)))
        sys.stdout.flush()
        if input() == "Y":
            return 0
        else:
            return 1


def request_index(index):
    print(index+1)
    sys.stdout.flush()
    return True if input() == "1" else False


def main():
    T, B = map(int, input().split())
    for _ in range(T):
        if solve(B):
            break
    return


if __name__ == '__main__':
    main()

