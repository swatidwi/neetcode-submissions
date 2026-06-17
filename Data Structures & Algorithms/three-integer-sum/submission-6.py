from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array first
        result = []
        nums.sort()

        for i,num in enumerate(nums):
            if num > 0:
                break

            if i>0 and num == nums[i-1]:
                continue

            j = i+1
            k = len(nums) -1

            while j<k:
                threeSum = num + nums[j]+nums[k]
                if threeSum == 0:
                    result.append([num,nums[j],nums[k]])
                    j = j+1
                    k = k-1
                    while nums[j] == nums[j-1] and j<k:
                        j = j +1

                elif threeSum > 0:
                    k = k-1
                else:
                    j = j+1
        return result

            

            