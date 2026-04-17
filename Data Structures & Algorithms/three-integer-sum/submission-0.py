class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Two pointer approach
        seen = set()
        seen.add(nums[0])
        triplets = set()
        for i in range(1, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if -(nums[i] + nums[j]) in seen:
                    triplet = [-(nums[i] + nums[j]), nums[i], nums[j]]
                    triplet.sort()
                    triplets.add(tuple(triplet))

            seen.add(nums[i])

        return [list(triplet) for triplet in triplets]