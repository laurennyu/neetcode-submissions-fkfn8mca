class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        seen = set()
        max_length = 0

        for num in nums_set:
            if num not in seen:
                seen.add(num)
                # Get the length of this num's sequence
                start = num
                end = num
                while start - 1 in nums_set:
                    start -= 1
                    seen.add(start)
                while end + 1 in nums_set:
                    end += 1
                    seen.add(end)
                max_length = max(max_length, end - start + 1)

        return max_length