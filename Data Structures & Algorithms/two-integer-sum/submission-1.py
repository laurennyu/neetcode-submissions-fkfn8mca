class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            val = nums[i]
            if target - val in seen.keys():
                return [seen[target - val], i]
            else:
                seen[val] = i