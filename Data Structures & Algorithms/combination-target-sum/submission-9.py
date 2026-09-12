class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        res = []

        def solve(candidate: list, idx: int, curr_sum: int):
            nonlocal nums, res, target

            if curr_sum == target:
                res.append(candidate.copy())
                return
            
            if curr_sum > target or idx >= len(nums):
                return

            # There are two choices: pick curr num or don't pick curr num
            if curr_sum + nums[idx] <= target:
                # Choose num
                candidate.append(nums[idx])
                solve(candidate, idx, curr_sum + nums[idx])
                candidate.pop()

            # Don't choose num
            solve(candidate, idx + 1, curr_sum)

        solve([], 0, 0)

        return res