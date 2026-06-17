import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = defaultdict(int)

        for num in nums:
            frequency_map[num] = frequency_map[num] + 1

        frequency_list = []
        for num,frequency in frequency_map.items():
            heapq.heappush(frequency_list, (-1*frequency,num))

            # if len(frequency_list) > k:
            #     heapq.heappop(frequency_list)

        # heapq.heapify_max(frequency_list)

        result = []
        while k>0:
            result.append(heapq.heappop(frequency_list)[1])
            k = k - 1

        return result


