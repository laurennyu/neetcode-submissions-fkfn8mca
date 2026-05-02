class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Let lis[j] = the longest inc. subsequence that includes nums[j]
        # from 0 to j
        lis = [1]
        global_max = 1
        for j in range(1, len(nums)):
            max_len = 1
            for i in range(j):
                if nums[i] < nums[j]:
                    max_len = max(max_len, lis[i] + 1)
            
            lis.append(max_len)
            global_max = max(global_max, max_len)

        return global_max