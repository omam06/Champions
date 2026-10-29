def merge_intervals(intervals):
    if intervals == []:
        return []
    intervals.sort()
    sorted_intervals = intervals

    merged = []
    merged.append(sorted_intervals[0])
    
    for remaining_interval in sorted_intervals[1:]:
        current = merged[-1]

        if remaining_interval[0] <= current[1]:
            current[1] = max(current[1],remaining_interval[1])
        else:
            merged.append(remaining_interval)

    return merged

intervals = [
    [1, 3],
    [4, 6],
    [8, 10],
    [9, 12]
]

print(merge_intervals(intervals))
