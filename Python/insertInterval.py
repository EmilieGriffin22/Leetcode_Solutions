#Not my first, but most elegant solution to insert intervals.
def insert(self, intervals, newInterval):
    i = 0
    merged = []

    while i < len(intervals) and intervals[i][-1] < newInterval[0]: 
        merged.append(intervals[i])
        i += 1 

    while i < len(intervals) and intervals[i][0] <= newInterval[-1]: 
        newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[-1], intervals[i][-1])]
        i += 1 
    merged.append(newInterval)

    while i < len(intervals): 
        merged.append(intervals[i])
        i += 1
    return merged 
    