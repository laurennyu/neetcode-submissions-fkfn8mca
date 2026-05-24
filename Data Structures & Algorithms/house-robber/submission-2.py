class Solution:
    def rob(self, nums: List[int]) -> int:
        # payout[i] is the maximum payout starting at house i
        payout = [0] * (len(nums) + 1)

        payout[-1] = 0
        payout[-2] = nums[-1]

        for i in range(len(nums)-2, -1, -1):
            # Take max of robbing this house or not
            payout[i] = max(nums[i] + payout[i+2],
                            payout[i+1])

        return payout[0]