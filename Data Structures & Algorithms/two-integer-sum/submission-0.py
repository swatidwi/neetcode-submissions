class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # map of number to index in nums

        for i,num1 in enumerate(nums):
            num2 = target - num1
            if num2 in seen:
                return [seen[num2], i]
            seen[num1] = i
        return []