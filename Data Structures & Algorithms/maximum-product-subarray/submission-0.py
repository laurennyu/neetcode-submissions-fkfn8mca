class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Edge cases: 0s and negatives have to be handled carefully
        # Let max_prod be the maximum product of a subarray that includes i,
        # min_prod be the minimum product of a subarray that includes i
        prev_max_prod = nums[0]
        prev_min_prod = nums[0]
        global_max = prev_max_prod

        for i in range(1, len(nums)):
            max_prod = max(nums[i], prev_max_prod * nums[i], prev_min_prod * nums[i])
            min_prod = min(nums[i], prev_max_prod * nums[i], prev_min_prod * nums[i])

            global_max = max(global_max, max_prod)

            prev_max_prod = max_prod
            prev_min_prod = min_prod

        return global_max