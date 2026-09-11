class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]] # Base case

        prev_perms = self.permute(nums[:-1])
        new_num = nums[-1]
        res = []
        for idx in range(len(nums)):
            res.extend([perm[0:idx] + [new_num] + perm[idx:] for perm in prev_perms])

        return res