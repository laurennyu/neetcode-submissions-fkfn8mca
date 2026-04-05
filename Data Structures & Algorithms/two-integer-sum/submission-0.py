class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            first = nums[i]
            for j in range(i+1, len(nums)):
                if first + nums[j] == target:
                    return [i, j]

        return False