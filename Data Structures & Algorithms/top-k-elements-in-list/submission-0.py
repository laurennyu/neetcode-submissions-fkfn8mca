class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Get frequencies
        freqs = {}
        for num in nums:
            if num in freqs:
                freqs[num] += 1
            else:
                freqs[num] = 1
        # Get k top frequencies
        freq_list = []
        for num, freq in freqs.items():
            freq_list.append((freq, num))
        
        freq_list = sorted(freq_list)
        output = []
        for i in range(k):
            idx = len(freq_list) - 1 - i
            output.append(freq_list[idx][1])

        return output