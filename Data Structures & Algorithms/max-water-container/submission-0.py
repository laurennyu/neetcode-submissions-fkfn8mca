class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_vol = 0
        while i < j:
            # Determine volume
            vol = (j - i) * min(heights[i], heights[j])
            max_vol = max(vol, max_vol)
            if heights[i] < heights[j]:
                # i is limiting the volume, move i
                i += 1
            else:
                j -= 1

        return max_vol