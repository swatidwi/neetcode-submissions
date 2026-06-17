class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        i = 0
        result = []
        while i<len(sorted_nums):
            num1 = sorted_nums[i]
            r = self.twoSum(sorted_nums[i+1:], num1*(-1))
            if (r):
                result.extend(r)
            while (i<len(sorted_nums) and sorted_nums[i] == num1):
                i+=1
        return result

    def twoSum(self, s_nums, target):
        result = []

        j,k=0,len(s_nums)-1

        while j<k:
            if (s_nums[j] + s_nums[k] == target):
                num1 = target*(-1)
                num2 = s_nums[j]
                num3 = s_nums[k]
                result.append([num1, num2, num3])
                j+=1
                k-=1
                while(j<k and s_nums[j]==num2 and s_nums[k] == num3):
                    j+=1
                    k-=1
            if (s_nums[j] + s_nums[k] < target):
                j+=1
            if (s_nums[j] + s_nums[k] > target):
                k-=1
        return result
        

