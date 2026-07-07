class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        def comb_sum(idx, target, comb):
            # Find all combinations that sum to target
            nonlocal nums, res

            # Base case: invalid idx
            if idx >= len(nums):
                return
            
            # Base case: reached target
            if nums[idx] == target:
                res.add(tuple(sorted(comb.copy() + [nums[idx]])))

            if nums[idx] < target:
                print(comb)
                # Take and repeat, or don't take this number
                comb_sum(idx, target-nums[idx], comb.copy() + [nums[idx]])

            comb_sum(idx+1, target, comb)

        comb_sum(0, target, [])
        return [list(comb) for comb in res]