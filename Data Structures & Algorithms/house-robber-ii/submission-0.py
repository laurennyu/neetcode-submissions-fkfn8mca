class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # Break into subproblems: exclude first house / last house
        def rob_subproblem(start, end):
            payout = [0] * (len(nums) + 1)
            payout[end+1] = 0
            payout[end] = nums[end]

            for i in range(end-1, start-1, -1):
                payout[i] = max(payout[i+1], nums[i] + payout[i+2])

            return payout[start]

        return max(rob_subproblem(0, len(nums)-2), rob_subproblem(1, len(nums)-1))