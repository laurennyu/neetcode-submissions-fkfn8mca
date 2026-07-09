class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump_potential = 1
        i = 0

        while i < len(nums) - 1:
            jump_potential = max(nums[i], jump_potential - 1)
            # Check if you are able to jump to next position
            if jump_potential > 0:
                # If yes, progress to next position
                i += 1
            else:
                print(i)
                return False

        return True