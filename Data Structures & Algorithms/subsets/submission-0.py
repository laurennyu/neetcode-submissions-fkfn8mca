class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res_len = len(res)
            for i in range(res_len):
                res.append(res[i].copy() + [num])

        return res