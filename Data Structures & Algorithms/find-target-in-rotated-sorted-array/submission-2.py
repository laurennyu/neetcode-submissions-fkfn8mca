class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1

        # Use binary search
        i = 0
        j = len(nums)-1
        while i < j:
            # print((i, j))
            mid = int((i + j)/2)
            if target == nums[mid]:
                return mid

            if target < nums[mid]:
                # Consider left
                if target >= nums[i]:
                    j = mid
                elif nums[i] > nums[mid]:
                    j = mid
                else:
                    # Look right
                    i = mid+1
            else: # target > nums[mid]
                if target <= nums[j]:
                    i = mid+1
                elif nums[mid] > nums[j]:
                    i = mid+1
                else:
                    j = mid

        if nums[i] == target:
            return i

        return -1 # target not found
