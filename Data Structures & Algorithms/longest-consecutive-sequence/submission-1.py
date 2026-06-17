class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consecutive_map = {}

        if not nums:
            return 0

        for num in nums:
            if num not in consecutive_map:
                consecutive_map[num] = ""
            previous_num = num-1
            if previous_num in consecutive_map:
                consecutive_map[previous_num] = num
            next_num = num+1
            if next_num in consecutive_map:
                consecutive_map[num] = next_num
        print(consecutive_map)

        max_length = 1
        for key,val in consecutive_map.items():
            length = 1
            while val != '':
                if val in consecutive_map:
                    length += 1
                    val = consecutive_map[val]
            max_length = max(length, max_length)

        return max_length
