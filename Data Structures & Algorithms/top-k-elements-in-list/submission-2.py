class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count_map = defaultdict(int)
        # result = []

        # for num in nums:
        #     new_count = count_map[num] + 1
        #     count_map[num] = new_count

        # arr = []
        # for num,count in count_map.items():
        #     arr.append([count, num])

        # arr.sort(reverse = True)

        # result_array = arr[:k]

        # return [num for _,num in result_array]

        ##############################

        count_map = defaultdict(int)
        result = []

        for num in nums:
            new_count = count_map[num] + 1
            count_map[num] = new_count

        frequency = [[] for i in range(len(nums) + 1)]

        for num, count in count_map.items():
            frequency[count].append(num)

        for i in range(len(frequency)-1, 0, -1):
            for num in frequency[i]:
                result.append(num)
                if len(result) == k:
                    return result





            
        