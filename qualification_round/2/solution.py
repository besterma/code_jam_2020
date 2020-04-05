
def generate_matching(S):
    start_string = []
    c_par = 0
    for s in S:
        s_int = int(s)
        if s_int > c_par:
            start_string.append("("*(s_int-c_par))
        else:
            start_string.append(")"*(c_par-s_int))
        start_string.append(s)
        c_par = s_int
    start_string.append(")"*c_par)
    return "".join(start_string)


T = int(input())

inputs = []

for i in range(T):
    inputs.append(input())

for i, s in enumerate(inputs):
    return_string = generate_matching(s)
    print("Case #{}: {}".format(i + 1, return_string))