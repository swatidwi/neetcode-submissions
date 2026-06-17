from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index_map = defaultdict(list)

        for index,num in enumerate(nums):
            num_to_index_map[num] = num_to_index_map[num] + [index]
            
        sorted_nums = sorted(nums)

        i= 0 
        j = len(nums) - 1


        while True:
            if sorted_nums[i] + sorted_nums[j] == target:
                result1 = num_to_index_map[sorted_nums[i]][0]
                if sorted_nums[i] == sorted_nums[j]:
                    result2 = num_to_index_map[sorted_nums[i]][1]
                else:
                    result2 = num_to_index_map[sorted_nums[j]][0]
                return sorted([result1,result2])
            if sorted_nums[i] + sorted_nums[j] > target:
                j = j-1
            else:
                i = i+1

        
