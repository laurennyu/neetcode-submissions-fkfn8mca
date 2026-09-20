class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            nums_len = len(res)
            for i in range(nums_len):
                new_subset = res[i].copy() + [num]
                res.append(new_subset)

        return res