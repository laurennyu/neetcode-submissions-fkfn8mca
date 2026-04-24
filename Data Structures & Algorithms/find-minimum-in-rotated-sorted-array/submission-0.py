class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if len = 1 or list is already sorted
        if nums[0] <= nums[-1]:
            return nums[0]

        # Use binary search to find the element where nums[i-1] > nums[i]
        left = 0
        right = len(nums) - 1
        while left < right:
            # There has to be at least 2 elements in the window
            mid = (left + right + 1) // 2
            if nums[mid - 1] > nums[mid]:
                # mid is the original start of the sequence
                return nums[mid]
            elif nums[mid] > nums[right]:
                # Look right
                left = mid
            else:
                # Look left
                right = mid

        