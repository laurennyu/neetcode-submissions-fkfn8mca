class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        res = []

        def solve(candidate: list, idx: int, curr_sum: int):
            nonlocal nums, res, target

            # There are two options: pick curr num or don't pick curr num
            curr_num = nums[idx]
            if curr_sum + curr_num == target:
                # Choose num and stop exploring- any subsequent num will be bigger than curr_num
                res.append(candidate.copy() + [curr_num])
                return

            elif curr_sum + curr_num < target:
                # Choose num and keep exploring
                candidate.append(curr_num)
                solve(candidate, idx, curr_sum + curr_num)
                candidate.pop()

                # Don't choose num
                if idx < len(nums) - 1:
                    solve(candidate, idx + 1, curr_sum)

        solve([], 0, 0)

        return res