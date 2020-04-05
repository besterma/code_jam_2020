def assign_schedule(activities):
    start_sorted = sorted(activities, key=lambda x: x["start"])
    end_sorted = sorted(activities, key=lambda x: x["end"])

    assignees = ["J", "C"]

    start_iter = iter(start_sorted)
    end_iter = iter(end_sorted)
    start_activity = next(start_iter)
    end_activity = next(end_iter)
    try:
        while True:
            if start_activity["start"] >= end_activity["end"]:
                assignees.append(end_activity["assignee"])
                end_activity = next(end_iter)
            else:
                start_activity["assignee"] = assignees.pop()
                start_activity = next(start_iter)

    except StopIteration:
        pass
    except IndexError:
        return "IMPOSSIBLE"

    return "".join(map(lambda x: x["assignee"], activities))



T = int(input())

test_cases = []

for i in range(T):
    N = int(input())
    activities = []
    for j in range(N):
        line = list(map(lambda x: int(x),input().split(" ")))
        activity = {"start": line[0], "end": line[1], "assignee": "X"}
        activities.append(activity)

    test_cases.append(activities)

for i, activities in enumerate(test_cases):
    schedule = assign_schedule(activities)
    print("Case #{}: {}".format(i + 1, schedule))


