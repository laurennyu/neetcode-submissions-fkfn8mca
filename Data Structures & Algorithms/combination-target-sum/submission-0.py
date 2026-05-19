class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        def dfs(i, curr_comb, curr_sum):
            nonlocal results
            if i >= len(nums):
                return

            if curr_sum == target:
                results.append(curr_comb)
                return

            if curr_sum > target:
                return

            dfs(i, curr_comb.copy() + [nums[i]], curr_sum + nums[i])
            dfs(i + 1, curr_comb.copy(), curr_sum)

        dfs(0, [], 0)
        return results