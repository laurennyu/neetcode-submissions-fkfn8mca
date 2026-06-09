class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Let lens[i] be the length of the longest strictly increasing subsequence including i
        lens = [1] * len(nums)
        global_max = 1
        for i in range(len(nums)-2, -1, -1):
            for j in range(i+1, len(nums)):
                # Check if i can extend subsequence from j
                if nums[i] < nums[j]:
                    lens[i] = max(lens[i], lens[j] + 1)

            global_max = max(global_max, lens[i])

        return global_max