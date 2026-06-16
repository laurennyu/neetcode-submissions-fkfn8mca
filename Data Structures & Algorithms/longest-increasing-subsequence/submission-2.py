class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Let lens[i] be the longest inc subseq starting at i and includes i
        lens = [1] * len(nums)
        global_max = 1
        for i in range(len(nums)-2, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    lens[i] = max(lens[i], 1+lens[j])
            
            global_max = max(global_max, lens[i])

        return global_max
