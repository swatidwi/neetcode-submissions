class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for num in nums:
        #     if nums.count(num) > 1:
        #         return True
        # return False

        # for i,num in enumerate(nums):
        #     if i!=len(nums)-1 and num in nums[i+1:]:
        #         print(i)
        #         return True
        # return False

        seen = {}
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                return True
        return False


