def findIntervals(arr: list[int]) -> str:
    arr = sorted(arr)
    intervals = [[arr[0]]]
    for item in arr[1:]:
        if item > intervals[-1][-1] + 1:
            intervals.append([item])
        else:
            if len(intervals[-1]) == 1:
                intervals[-1].append(item)
            else:
                intervals[-1][-1] += 1
    return ','.join("-".join(str(bound) for bound in interval)
                    if len(interval) == 2 else str(interval[0]) for interval in intervals)

print(findIntervals([1,2]))