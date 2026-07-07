class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        base_idx = ord("A")

        for task in tasks:
            freq[ord(task) - base_idx] += 1

        # Get most frequent item
        max_f = max(freq)
        # Count how much "overflow" occurs (if multiple tasks have max freq)
        max_count = 0
        for count in freq:
            if count == max_f:
                max_count += 1

        # Calculate space needed for the tasks if schedule not completely full
        res = ((max_f - 1) * (n + 1)) + max_count

        return max(res, len(tasks))