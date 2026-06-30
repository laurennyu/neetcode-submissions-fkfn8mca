class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Store results in a set to avoid duplicates
        res = set()
        seen = set()
        seen.add(nums[0])
        for i in range(1, len(nums)-1):
            for j in range(i+1, len(nums)):
                if -(nums[i] + nums[j]) in seen:
                    # Sort individual answers to handle duplicates
                    res.add(tuple(sorted([-(nums[i] + nums[j]), nums[i], nums[j]])))

            # Only add to seen set after visited by i to avoid double counting
            seen.add(nums[i])

        return [list(tup) for tup in res]