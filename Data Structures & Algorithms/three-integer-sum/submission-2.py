class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        for i in range(len(nums)-1):
            # Like a two-sum problem in this loop
            seen = set()
            for j in range(i+1, len(nums)):
                num_sum = nums[i] + nums[j]
                if -num_sum in seen:
                    # This is a valid triplet
                    triplets.add(tuple(sorted([nums[i], nums[j], -num_sum])))
                seen.add(nums[j])

        return [list(tup) for tup in triplets]