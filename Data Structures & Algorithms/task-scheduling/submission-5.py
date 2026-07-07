class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter

        freq = Counter(tasks)
        freq_list = list(freq.values())

        # Get most frequent item
        max_f = max(freq_list)
        # Count how much "overflow" occurs (if multiple tasks have max freq)
        max_count = 0
        for count in freq_list:
            if count == max_f:
                max_count += 1

        # Calculate space needed for the tasks if schedule not completely full
        res = ((max_f - 1) * (n + 1)) + max_count

        return max(res, len(tasks))