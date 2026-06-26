class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Given: intervals is non-overlapping, sorted in ascending order by start
        # Find position to insert new interval,
        # i.e. prev interval start <= new interval start < next interval start
        target_idx = 0
        while target_idx < len(intervals) and intervals[target_idx][0] < newInterval[0]:
            target_idx += 1

        # Determine if merging is necessary
        if target_idx > 0:
            # Look at previous interval
            if newInterval[0] <= intervals[target_idx - 1][1]:
                target_idx -= 1
                # Merge with previous, edit prev interval in place
                intervals[target_idx][1] = max(intervals[target_idx][1], newInterval[1])
            else:
                intervals.insert(target_idx, newInterval)
        else:
            # if 0, insert at front, don't need to look at if merging is necessary with prev interval
            intervals.insert(target_idx, newInterval)
        
        # Check if we need to merge with next interval(s)
        while target_idx + 1 < len(intervals) and intervals[target_idx + 1][0] <= intervals[target_idx][1]:
            intervals[target_idx][1] = max(intervals[target_idx][1], intervals[target_idx + 1][1])
            intervals.pop(target_idx + 1)
            
            # if len(intervals), insert at end, don't need to look at if merging is necessary with next interval

        return intervals