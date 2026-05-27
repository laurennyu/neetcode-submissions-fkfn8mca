class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max = nums[0]
        curr_sum = nums[0]
        for i in range(1, len(nums)):
            if curr_sum < 0:
                # Don't include the previous subarray; start over
                curr_sum = nums[i]
            else:
                # Include previous subarray and add current num
                curr_sum += nums[i]
                
            global_max = max(global_max, curr_sum)

        return global_max