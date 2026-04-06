import heapq
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
        heap = [(-freq, num) for num, freq in freqs.items()]
        heapq.heapify(heap)
        output = []
        for i in range(k):
            output.append(heapq.heappop(heap)[1])
        # for num, freq in freqs.items():
        #     heap = heapq.heappush((freq, num))
        
        # freq_list = sorted(freq_list)
        # output = []
        # for i in range(k):
        #     idx = len(freq_list) - 1 - i
        #     output.append(freq_list[idx][1])

        return output