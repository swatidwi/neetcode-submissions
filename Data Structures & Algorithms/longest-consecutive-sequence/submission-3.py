class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # from nums, we can create a map where key is a number and value is the next number (num+1) if it exists in nums

        # so basically for each num, check 2 things:
        # 1) if num-1 is in nums, add nums-1 as the key and num as the value
        # 2) if num+1 is in nums, add num as the key and num+1 as the value

        result = 0
        consecutive_map = {}
        for num in nums:
            if num-1 in nums:
                consecutive_map[num-1] = num
            if num+1 in nums:
                consecutive_map[num] = num+1
            else:
                consecutive_map[num] = ""

        l = 1
        for num in consecutive_map.keys():
            while consecutive_map[num] != "":
                next_num = consecutive_map[num]
                l += 1
                num = next_num
            result = max(result,l)
            l = 1

        return result

