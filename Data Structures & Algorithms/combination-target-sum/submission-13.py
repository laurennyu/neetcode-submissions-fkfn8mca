class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def solve(idx, comb, curr_sum):
            nonlocal res, nums, target
            if curr_sum == target:
                res.append(comb.copy())
                return
            if idx >= len(nums):
                return

            curr_num = nums[idx]
            if target - curr_sum >= curr_num:
                comb.append(curr_num)
                solve(idx, comb, curr_sum + curr_num)
                comb.pop()

            solve(idx+1, comb, curr_sum)

        solve(0, [], 0)
        return res