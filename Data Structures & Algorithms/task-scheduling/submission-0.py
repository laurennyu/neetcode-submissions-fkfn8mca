class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        import numpy as np
        freq = Counter(tasks)
        freq_list = [count for count in freq.values()]
        freq_list.sort()

        # Get most frequent item
        max_f = freq_list.pop()
        max_len = ((max_f - 1) * (n + 1)) + 1

        # Fill in pockets
        free_spots = (max_f - 1) * n
        idx = len(freq_list) - 1
        while free_spots > 0 and idx >= 0:
            spots_to_fill = min(min(max_f - 1, freq_list[idx]), free_spots)
            free_spots -= spots_to_fill
            freq_list[idx] -= spots_to_fill
            idx -= 1

        return max_len + int(np.sum(freq_list))
            