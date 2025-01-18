# O(nlogn) solution using sorting.
def merge(self, intervals):
    intervals = sorted(intervals)
    j = 0
    for i in range(1, len(intervals)):
        if intervals[i][0] <= intervals[j][-1]: 
            intervals[j][-1] = max(intervals[j][-1], intervals[i][-1])
        else: 
            j += 1
            intervals[j] = intervals[i]
    return intervals[:j + 1]